from flask import Blueprint, request
from .. services.product_service import ProductService
from .. models.Database import Database
from .. utils.cookie import verify_token
from functools import wraps
import json, jwt

bp = Blueprint('products', __name__, url_prefix='/api/product')
db_session = Database.get_session()

def get_uid():
    session = request.cookies.get('session')
    return jwt.decode(session, options={"verify_signature": False}).get('user_id')

@bp.route('/list', methods=['GET'])
def register():
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

@bp.route('/inventory', methods=['GET'])
@auth_required
def get_item_data():
    user_id = get_uid()
    return ProductService.get_inventory(session=db_session, user_id=user_id)

@bp.route('/getitem', methods=['POST'])
def getitem():
    item_type = request.json['type']
    rarity = request.json['rarity']
    item_name = request.json['name']

    item = None

    return {'status': 'ok', 'item': item}, 200

@bp.route('/sell', methods=['POST'])
def sell():
    return {'status': 'under construction'}
    