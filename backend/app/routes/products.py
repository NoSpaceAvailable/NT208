from flask import Blueprint, request, jsonify
from .. services.product_service import *

bp = Blueprint('products', __name__, url_prefix='/api')

@bp.route('/list', methods=['GET'])
def register():
    return jsonify({"list":"ok"})