from flask import Blueprint, request, make_response, redirect, jsonify
from ..services.auth_service import *
from .. services.user_service import UserService
from ..utils.cookie import *
from ..services.mail_service import EmailService
import secrets
from concurrent.futures import ThreadPoolExecutor
from cachetools import TTLCache
from .. import limiter
from .. global_config import oauth2_config, site_url
import httpx
from .. models.Database import Database

bp = Blueprint("auth", __name__, url_prefix="/api/auth")
cache = TTLCache(maxsize=30, ttl=180)
executor = ThreadPoolExecutor(max_workers=5)

VERIFICATION_CODE_MAX_UPBOUND = 1000000
general_msg = "If your email is available, a 6-digit code will be sent to your email. The code will expire in 3 minutes."

def get_session():
    return Database.get_session()

@bp.route("/register", methods=["POST"])
@limiter.limit("5 per 3 minute")
def register():
    try:
        username = request.json["username"]
        password = request.json["password"]
        email = request.json["email"]
    except KeyError:
        return jsonify({"status": "Missing required fields"}), 400

    if user_exist(username=username, email=email) or cache.get(email):
        return jsonify({"status": general_msg}), 403

    verification_code = f"{secrets.randbelow(VERIFICATION_CODE_MAX_UPBOUND):06d}"

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
@limiter.limit("5 per 3 minute")
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
@limiter.limit("10 per minute")
def login():
    try:
        username = request.json["username"]
        password = request.json["password"]
    except Exception:
        return jsonify({"status": "Missing required fields"}), 400

    if check_user(username=username, password=password):
        response = make_response({"status": "ok"})
        response.set_cookie("session", 
                            sign_token({
                                "username": username,
                                "user_id": UserService.get_user_id(session, username)
                            }), 
                            samesite = "Lax",
                            max_age = 600,
                            secure = False,
                            httponly = True,
                        )
        return response

    return jsonify({"status": "Invalid credentials"}), 401

@bp.route("/google", methods=["POST"])
@limiter.limit("5 per 3 minute")
def handle_oauth2():
    try:
        code = request.json["code"]
        client_id = oauth2_config["client_id"]
        client_secret = oauth2_config["client_secret"]
        grant_type = oauth2_config["grant_type"]
        session = get_session()
        res = httpx.post(
            "https://oauth2.googleapis.com/token",
            data = {
                "code": code,
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": grant_type,
                "redirect_uri": site_url
            }
        )
        if res.status_code == 200:
            access_token = res.json().get("access_token")
            user_info = httpx.get(
                "https://www.googleapis.com/oauth2/v2/userinfo",
                headers = {
                    "Authorization": f"Bearer {access_token}"
                }
            )
            if user_info.status_code == 200:
                user_info = user_info.json()
                email = user_info.get("email")
                username = user_info.get("name")
                if not user_exist(username=username, email=email):
                    create_user(username=username, password=None, email=email, is_oauth2=True)
                response = make_response({"status": "ok"})
                response.set_cookie("session", 
                                    sign_token({
                                        "username": username,
                                        "user_id": UserService.get_user_id(session, username),
                                    }), 
                                    samesite = "Lax",
                                    max_age = 3600,
                                    secure = False,
                                    httponly = True,
                                )
                return response
        return jsonify({"status": "Failed to get user info"}), 401
    except Exception:
        return jsonify({"status": "Missing required fields"}), 400

@bp.route("/check", methods=["GET"])
def check_auth():
    token = request.cookies.get("session")
    if token and verify_token(token):
        return { "status": "ok" }
    return { "status": "unauthorized" }, 401

@bp.route("/logout", methods=["GET"])
def logout():
    response = make_response(redirect("/"))
    response.delete_cookie("session")
    return response

@bp.route("/reset", methods=["POST"])
def reset():
    # TODO: Implement password reset logic here
    return jsonify({"status": "ok"})