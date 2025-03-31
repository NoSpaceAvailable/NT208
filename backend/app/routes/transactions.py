from flask import Blueprint, request
from .. services.transaction_service import *
from .. services.transaction_service import TransactionService
from .. services.user_service import UserService
from .. services.history_service import HistoryService
from .. utils.cookie import verify_token
from .. models.Database import Database
import jwt

bp = Blueprint('transactions', __name__, url_prefix='/api/transaction')
session = Database.get_session()

def get_payload(token: str):
    return jwt.decode(
        jwt=token,
        options={"verify_signature": False}
    )

@bp.before_request
def check_auth():
    session = request.cookies.get('session')
    if not session or not verify_token(session):
        return {"status": "unauthorized"}, 401

@bp.route('/create-wallet', methods=['GET'])
def create():
    _session = request.cookies.get('session')
    payload = get_payload(_session)
    user_id = payload.get('user_id')
    username = payload.get('username')
    if not user_id or not username:
        return {"status": "unauthorized"}, 401
    
    if address := TransactionService.safe_create_wallet(session, user_id, username):
        return {"status": "ok", "address": address}
    return {"status": "failed"}, 500

@bp.route('/balance', methods=['GET'])
def get_balance():
    _session = request.cookies.get('session')
    payload = get_payload(_session)
    username = payload.get('username')
    if not username:
        return {"status": "unauthorized"}, 401
    
    if balance := TransactionService.safe_get_balance(session, username):
        return {"status": "ok", "balance": balance}
    return {"status": "failed"}, 500

@bp.route('/add', methods=['POST'])
def add():
    data = request.json
    _address = data.get('address')
    _amount = data.get('amount')

    if not _address or not _amount or _amount <= 0:
        return {"status": "failed"}, 500
    
    try:
        TransactionService.safe_add(
            session=session,
            wallet_address=_address,
            amount=_amount
        )
        return {"status": "ok"}
    except Exception as e:
        return {"status": "failed"}, 500

@bp.route('/pay', methods=['POST'])
def pay():
    data = request.json
    _to = data.get('to')
    _amount = data.get('amount')

    if not _to or not _amount:
        return {"status": "failed"}, 500
    
    _session = request.cookies.get('session')
    payload = get_payload(_session)
    sender_id = payload.get('user_id')
    
    if TransactionService.safe_transaction(
        session=session,
        sender_id=sender_id,
        receiver_address=_to,
        amount=_amount
    ):
        return {"status": "ok"}
    return {"status": "failed"}, 500

@bp.route('/history', methods=['GET'])
def get_history():
    _session = request.cookies.get('session')
    payload = get_payload(_session)
    username = payload.get('username')
    if not username:
        return {"status": "unauthorized"}, 401
    
    if history := HistoryService.safe_get_history_record(session=session, username=username):
        return {"status": "ok", "history": history}
    return {"status": "failed"}, 500


