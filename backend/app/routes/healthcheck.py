from flask import Blueprint, request, jsonify

bp = Blueprint('healthcheck', __name__, url_prefix='/api')

@bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status":"ok"})