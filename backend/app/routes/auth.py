from flask import Blueprint, request, make_response, redirect, jsonify
from ..services.auth_service import *
from ..utils.cookie import *
from ..services.mail_service import EmailService
import secrets
from concurrent.futures import ThreadPoolExecutor
from cachetools import TTLCache

bp = Blueprint("auth", __name__, url_prefix="/api/auth")
cache = TTLCache(maxsize=30, ttl=180)
executor = ThreadPoolExecutor(max_workers=5)

VERIFICATION_CODE_MAX = 999999
general_msg = "If your email is available, a 6-digit code will be sent to your email. The code will expire in 3 minutes."

@bp.route("/register", methods=["POST"])
def register():
    try:
        username = request.json["username"]
        password = request.json["password"]
        email = request.json["email"]
    except KeyError:
        return jsonify({"status": "Missing required fields"}), 400

    if user_exist(username=username, email=email) or cache.get(email):
        return jsonify({"status": general_msg})

    verification_code = f"{secrets.randbelow(1000000):06d}"

    cache[email] = { 
        'code': verification_code, 
        'username': username,
        'password': password
    }

    try:
        executor.submit(EmailService, email, verification_code)
    except Exception as e:
        return jsonify({"status": "Failed to send verification email"}), 500

    return jsonify({"status": general_msg})

@bp.route("/verify", methods=["POST"])
def verify():
    try:
        email = request.json["email"]
        code = request.json["code"]
    except KeyError:
        return jsonify({"status": "Missing required fields"}), 400

    user = cache.get(email)
    if not user:
        return jsonify({"status": "Failed to verify"}), 401

    if user.get('code') != code:
        return jsonify({"status": "Failed to verify"}), 401

    if create_user(username=user.get('username'), password=user.get('password'), email=email):
        del cache[email]
        return jsonify({"status": "Verification successful. You can now login."})

    return jsonify({"status": "Failed to verify"}), 401

@bp.route("/login", methods=["POST"])
def login():
    try:
        username = request.json["username"]
        password = request.json["password"]
    except KeyError:
        return jsonify({"status": "Missing required fields"}), 400

    if check_user(username=username, password=password):
        response = make_response(redirect("/"))
        token = sign_token({"username": username})
        response.set_cookie("session", 
                            value=token,
                            secure=False,
                            httponly=True,
                            samesite="Lax")
        return response

    return jsonify({"status": "Invalid credentials"}), 401

@bp.route("/logout", methods=["GET"])
def logout():
    response = make_response(redirect("/"))
    response.delete_cookie("session")
    return response

@bp.route("/reset", methods=["POST"])
def reset():
    # Implement password reset logic here
    return jsonify({"status": "ok"})