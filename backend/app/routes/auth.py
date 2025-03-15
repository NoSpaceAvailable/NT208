from flask import Blueprint, request, jsonify
from .. services.auth_service import *

bp = Blueprint('auth', __name__, url_prefix='/api')

@bp.route('/register', methods=['POST'])
def register():
    return jsonify({"register":"ok"})

@bp.route('/login', methods=['POST'])
def login():
    return jsonify({"login":"ok"})

@bp.route('/logout', methods=['POST'])
def logout():
    return jsonify({"logout":"ok"})

@bp.route('/reset', methods=['POST'])
def reset():
    return jsonify({"reset":"ok"})

