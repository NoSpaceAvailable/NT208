from flask import Blueprint, request, jsonify
from .. services.auth_service import *
from .. models.User import User

bp = Blueprint('auth', __name__, url_prefix='/api')

@bp.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    new_user = User(1, username, email, password, None)
    try:
        return jsonify({
            "status":"ok", 
            "token": sign(new_user)
        })
    except Exception as e:
        return jsonify({"status":"failed", "message":str(e)})


@bp.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    new_user = User(1, username, email, password, None)
    try:
        return jsonify({
            "status":"ok", 
            "token": sign(new_user)
        })
    except Exception as e:
        return jsonify({"status":"failed", "message":str(e)})

@bp.route('/logout', methods=['POST'])
def logout():
    return jsonify({"logout":"ok"})

@bp.route('/reset', methods=['POST'])
def reset():
    return jsonify({"reset":"ok"})

