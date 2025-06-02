from flask import Blueprint, request, redirect  
from app.services.transaction_service import *
from app.services.transaction_service import TransactionService
from app.services.history_service import HistoryService
from app.services.product_service import ProductService
from app.services.profile_service import ProfileService
from app.utils.cookie import verify_token
from app.models.Database import Database
from app.models.enumtypes.HistoryStatus import HistoryStatus
from app.models.enumtypes.HistoryType import HistoryType
from app.utils.momo.momo import Momo, generate_transaction_hash
from base64 import b64decode
import jwt
from datetime import datetime, timezone

bp = Blueprint('transactions', __name__, url_prefix='/api/transaction')
momo = Momo()

# legacy code
def get_payload(token: str):
    return jwt.decode(
        jwt=token,
        options={"verify_signature": False}
    )

def get_uid():
    session = request.cookies.get('session')
    return jwt.decode(session, options={"verify_signature": False}).get('user_id')

def get_current_time() -> str:
    local_time = datetime.now()
    utc_time = local_time.astimezone(timezone.utc)
    return utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")

@bp.before_request
def check_auth():
    session = request.cookies.get('session')
    if not session or not verify_token(session):
        return {"status": "unauthorized"}, 401

def get_session():
    return Database.get_session()

@bp.route('/create-wallet', methods=['GET'])
def create():
    session = get_session()
    try:
        _session = request.cookies.get('session')
        payload = get_payload(_session)
        user_id = payload.get('user_id')
        username = payload.get('username')
        if address := TransactionService.safe_create_wallet(session, user_id, username):
            session.commit()
            return {"status": "ok", "address": address}
        return {"status": "failed"}, 500
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()

@bp.route('/balance', methods=['GET'])
def get_balance():
    session = get_session()
    try:
        _session = request.cookies.get('session')
        payload = get_payload(_session)
        username = payload.get('username')
        balance = TransactionService.safe_get_balance(session, username)
        if balance != None:
            return {"status": "ok", "balance": balance}
        return {"status": "failed"}, 500
    finally:
        session.close()

@bp.route('/add', methods=['POST'])
def add():
    data = request.json
    _address = data.get('address')
    _amount = data.get('amount')

    if not _address or not _amount or _amount <= 0:
        return {"status": "failed"}, 500
    try:
        pay_url = momo.create_payment_url(
            amount=int(_amount), 
            wallet_address=_address,
            message="To: " + _address
        )
        return {"status": "ok", "pay_url": pay_url}
    except Exception as e: 
        print(e, flush=True)
        return {"status": "failed"}, 500

@bp.route('/trade', methods=['POST'])
def trade_item():
    session = get_session()
    try:
        data = request.json
        item_id = data['item_id']
        buyer_id = get_uid()
        _session = request.cookies.get('session')
        payload = get_payload(_session)
        buyer_username = payload.get('username')
        with session.begin():
            seller_user_item = ProductService.get_product_item(session=session, user_item_id=item_id)
            if not seller_user_item.for_sale:
                return {'status': 'failed'}, 400
            if seller_user_item.user_id == buyer_id:
                return {'status': 'failed'}, 400
            balance = TransactionService.safe_get_balance(session=session, username=buyer_username)
            item_info = seller_user_item.to_dict()
            item_price = item_info.get('item').get('price')
            if balance < item_price:
                return {'status': 'failed', 'msg': 'insufficient balance'}, 400
            profile = ProfileService.safe_get_profile(session=session, user_id=seller_user_item.user_id)
            seller_address = profile.wallet_address
            if not TransactionService.safe_transaction(
                session=session,
                sender_id=buyer_id,
                receiver_address=seller_address,
                amount=item_price
            ):
                return {'status': 'failed', 'msg': 'something went wrong'}, 500
            seller_user_item.user_id = buyer_id
        session.commit()
        return {'status': 'success'}
    except Exception as e:
        session.rollback()
        error(f"Error while trading: {e}", __name__)
        return {'status': 'failed', 'msg': 'something went wrong'}, 500
    finally:
        session.close()

@bp.route('/history', methods=['GET'])
def get_history():
    session = get_session()
    try:
        _session = request.cookies.get('session')
        payload = get_payload(_session)
        username = payload.get('username')
        if history := HistoryService.safe_get_history_records(session=session, username=username):
            return {"status": "ok", "history": history}
        return {"status": "failed"}, 500
    finally:
        session.close()

@bp.route('/confirm', methods=['GET'])
def confirm():
    session = get_session()
    try:
        data = request.args
        order_id = data.get('orderId')
        amount = data.get('amount')
        order_info = data.get('orderInfo')
        message = data.get('message')
        timestamp_base64 = data.get('extraData')
        if message != "Thành công.":
            return {"status": "failed"}, 500
        target_wallet = order_info.split("To: ")[1]
        transaction_hash = generate_transaction_hash(
            sender_hash=target_wallet,
            receiver_hash=target_wallet,
            amount=int(amount),
            timestamp=b64decode(timestamp_base64).decode('utf-8')
        )
        if transaction_hash == order_id:
            record = HistoryService.select_one_by_transaction_hash(session=session, transaction_hash=transaction_hash)
            if record == None:
                TransactionService.safe_add(
                    session=session,
                    wallet_address=target_wallet,
                    amount=int(amount)
                )
                HistoryService.safe_create_transaction_history(
                    session=session,
                    sender_address=target_wallet,
                    receiver_address=target_wallet,
                    amount=int(amount),
                    timestamp=b64decode(timestamp_base64).decode('utf-8'),
                    message="To: " + target_wallet,
                    status=HistoryStatus.COMPLETED.value,
                    transaction_type=HistoryType.TOPUP.value
                )
                session.commit()
                return redirect('/add')
            else:
                return {"status": "failed"}, 500
        else:
            return {"status": "failed"}, 500
    except Exception as e:
        session.rollback()
        print("Error:", e, flush=True)
        return {"status": "failed"}, 500
    finally:
        session.close()

@bp.route('/pay', methods=['POST'])
def pay():
    session = get_session()
    data = request.json
    _to = data.get('to')
    _amount = data.get('amount')

    if not _to or not _amount:
        return {"status": "failed"}, 400
    
    _session = request.cookies.get('session')
    payload = get_payload(_session)
    sender_username = payload.get('username')
    sender_id = UserService.get_user_id(session, sender_username)
    
    if TransactionService.safe_transaction(
        session=session,
        sender_id=sender_id,
        receiver_address=_to,
        amount=_amount
    ) == True:
        sender_address = UserService.get_wallet_address(session=session, user_id=sender_id)
        if HistoryService.safe_create_transaction_history(
            session=session,
            sender_address=sender_address,
            receiver_address=_to,
            amount=_amount,
            timestamp=get_current_time(),
            message="To: " + _to,
            status=HistoryStatus.COMPLETED.value,
            transaction_type=HistoryType.TRANSFER.value
        ) == True:
            session.commit()
            return {"status": "ok"}
        session.rollback()
        return {"status": "failed"}, 400
    return {"status": "failed"}, 400
