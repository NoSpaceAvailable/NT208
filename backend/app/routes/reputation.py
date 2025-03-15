from flask import Blueprint, request, jsonify
from .. services.reputation_service import *

bp = Blueprint('reputaions', __name__, url_prefix='/api')

@bp.route('/comments', methods=['GET'])
def get_comments():
    return jsonify({"comments":"ok"})

@bp.route('/rates', methods=['GET'])
def get_rates():
    return jsonify({"rates":"ok"})