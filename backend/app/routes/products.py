from flask import Blueprint, request
from .. services.product_service import ProductService
from .. models.Database import Database
from .. utils.cookie import verify_token
from .. services.profile_service import ProfileService
from .. services.transaction_service import TransactionService
from .. services.user_service import UserService
from functools import wraps
import json, jwt

bp = Blueprint('products', __name__, url_prefix='/api/product')

def get_session():
    return Database.get_session()

def get_uid():
    session = request.cookies.get('session')
    return jwt.decode(session, options={"verify_signature": False}).get('user_id')

def get_username():
    session = request.cookies.get('session')
    return jwt.decode(session, options={"verify_signature": False}).get('username')

def user_created_profile(user_id) -> bool:
    session = get_session()
    try:
        user_id = get_uid()
        return ProfileService.safe_get_profile(session, user_id) is not None
    finally:
        session.close()

@bp.route('/list', methods=['GET'])
def list_items():
    if request.args.get('featured'):
        featured_data = open('/app/app/misc/featured.json').read()
        return json.loads(featured_data)
    json_data = open('/app/app/misc/skin_data.json').read()
    return json.loads(json_data)

def auth_required(f):
    @wraps(f)
    def check_auth(*args, **kwargs):
        session = request.cookies.get('session')
        if not session or not verify_token(session):
            return {'status': 'unauthorized'}, 401
        return f(*args, **kwargs)
    return check_auth

@bp.route('/inventory/<uid>', methods=['GET'])
@auth_required
def show_user_inventory(uid):
    """Also let people see other's items, like Steam do"""
    session = get_session()
    try:
        if uid == 'me':
            user_id = get_uid()
        else:
            user_id = uid
        return ProductService.get_inventory(session=session, user_id=user_id)
    finally:
        session.close()

@bp.route('/sell', methods=['POST'])
@auth_required
def sell():
    """simply put an item to for sale state"""
    user_id = get_uid()
    session = get_session()
    try:
        if not user_created_profile(user_id=user_id):
            return {'status': 'failed', 'msg': 'please create a wallet and profile first'}, 400
        data = request.json
        item_id = data['item_id']
        if not ProductService.item_is_belong_to(session=session, user_item_id=item_id, user_id=user_id):
            return {'status': 'failed', 'msg': 'you does not own this item'}, 400
        sale_status = True
        if data.get('rollback_sell_state') == True:
            sale_status = False
        if not ProductService.update_sale_status(session=session, user_item_id=item_id, new_sale_status=sale_status):
            return {'status': 'failed', 'msg': 'something went wrong'}, 400
        session.commit()
        return {'status': 'success', 'msg': 'done'}
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

@bp.route('/buy', methods=['POST'])
@auth_required
def buy():
    user_id = get_uid()
    username = get_username()
    session = get_session()
    try:
        if not user_created_profile(user_id=user_id):
            return {'status': 'failed', 'msg': 'please create a wallet and profile first'}, 400
        data = request.json
        item_id = data['item_id']
        if ProductService.item_is_belong_to(session=session, user_item_id=item_id, user_id=user_id):
            return {'status': 'failed', 'msg': 'you cannot buy your own item'}, 400
        
        current_balance = TransactionService.safe_get_balance(session=session, username=username)
        item = ProductService.get_product_item(session=session, user_item_id=item_id)

        if not item.for_sale:
            return {'status': 'failed', 'msg': 'this item is not for sale'}, 400

        verbose_data = item.to_dict()
        if current_balance < verbose_data['item']['price']:
            return {'status': 'failed', 'msg': 'you do not have enough money'}, 400
        
        receiver_address = UserService.get_wallet_address(session=session, user_id=item.user_id)
        if not receiver_address:
            return {'status': 'failed', 'msg': 'seller wallet address not found'}, 400
        
        if not TransactionService.safe_transaction(
                session=session, 
                sender_id=user_id, 
                receiver_address=receiver_address, 
                amount=verbose_data['item']['price']
            ):
            return {'status': 'failed', 'msg': 'something went wrong'}, 400
        
        if not ProductService.transfer_ownership_to(session=session, user_item_id=item_id, new_user_id=user_id):
            return {'status': 'failed', 'msg': 'something went wrong'}, 400
        
        if not ProductService.update_sale_status(session=session, user_item_id=item_id, new_sale_status=False):
            return {'status': 'failed', 'msg': 'something went wrong'}, 400
        
        session.commit()
        return {'status': 'success', 'msg': 'done'}
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

@bp.route('/seller', methods=['GET'])
@auth_required
def get_seller():
    kind = request.args.get('kind')
    name = request.args.get('name')
    session = get_session()
    try:
        if not kind or not name:
            return []
        return ProductService.get_seller_list(session=session, kind=kind, name=name)
    finally:
        session.close()

