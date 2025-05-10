from flask import Blueprint, Response
from .. services.product_service import *
import json

bp = Blueprint('products', __name__, url_prefix='/api/product')

@bp.route('/list', methods=['GET'])
def register():
    json_data = open('/app/app/misc/skin_data.json').read()
    return json.loads(json_data)