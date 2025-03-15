from flask import Blueprint, request, jsonify
from .. services.transaction_service import *

bp = Blueprint('transactions', __name__, url_prefix='/api')

@bp.route('/transactions', methods=['GET'])
def get_comments():
    return jsonify({"transactions":"ok"})

@bp.route('/history', methods=['GET'])
def get_rates():
    return jsonify({"history":"ok"})