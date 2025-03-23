from flask import Blueprint
from .. services.product_service import *

bp = Blueprint('products', __name__, url_prefix='/api/product')

@bp.route('/list', methods=['GET'])
def register():
    return {"status":"ok"}