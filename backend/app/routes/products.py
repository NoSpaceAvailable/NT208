from flask import Blueprint, request
from .. services.product_service import ProductService
from .. models.Database import Database
from .. utils.cookie import verify_token
from .. services.profile_service import ProfileService
from functools import wraps
import json, jwt
from itertools import islice

bp = Blueprint('products', __name__, url_prefix='/api/product')
db_session = Database.get_session()

def get_uid():
    session = request.cookies.get('session')
    return jwt.decode(session, options={"verify_signature": False}).get('user_id')

def user_created_profile(user_id) -> bool:
    user_id = get_uid()
    return ProfileService.safe_get_profile(db_session, user_id) is not None

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
    if uid == 'me':
        user_id = get_uid()
    else:
        user_id = uid
    return ProductService.get_inventory(session=db_session, user_id=user_id)

@bp.route('/sell', methods=['POST'])
@auth_required
def sell():
    """simply put an item to for sale state"""
    user_id = get_uid()
    if not user_created_profile(user_id=user_id):
        return {'status': 'failed', 'msg': 'please create a wallet and profile first'}, 400
    data = request.json
    item_id = data['item_id']
    if not ProductService.item_is_belong_to(session=db_session, user_item_id=item_id, user_id=user_id):
        print("CANT SELL")
        return {'status': 'failed', 'msg': 'you does not own this item'}, 400
    if not ProductService.update_sale_status(session=db_session, user_item_id=item_id, new_sale_status=True):
        return {'status': 'failed', 'msg': 'something went wrong'}, 400
    return {'status': 'success', 'msg': 'the item has been put to sale state, now it\'s visible on marketplace'}

@bp.route('/seller', methods=['GET'])
@auth_required
def get_seller():
    kind = request.args.get('kind')
    name = request.args.get('name')
    if not kind or not name:
        return []
    return ProductService.get_seller_list(session=db_session, kind=kind, name=name)

