from flask import Blueprint, request, make_response, redirect
from ..services.auth_service import *
from ..utils.cookie import *

bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@bp.route("/register", methods=["POST"])
def register():
    username = request.json["username"]
    password = request.json["password"]
    email = request.json["email"]

    if user_exist(username=username, email=email):
        return {"status":"user already exists"}

    if create_user(username=username, email=email, password=password):
        return {"status":"ok"}
    
    return {"status":"user already exists"}

@bp.route("/login", methods=["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]

    if check_user(username=username, password=password):
        response = make_response(redirect("/"))
        token = sign_token({"username": username})
        response.set_cookie("session", 
                            value = token,
                            secure = False,
                            httponly = True)
        return response
    
    return {"status":"invalid credentials"}, 401

@bp.route("/logout", methods=["GET"])
def logout():
    response = make_response(redirect("/"))
    response.delete_cookie()
    return response

@bp.route("/reset", methods=["POST"])
def reset():
    return {"status":"ok"}

