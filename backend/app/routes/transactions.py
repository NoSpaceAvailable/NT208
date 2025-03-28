from flask import Blueprint, request
from .. services.transaction_service import *
from .. services.transaction_service import TransactionService
from .. utils.cookie import verify_token
from .. models.Database import Database
import jwt

bp = Blueprint('transactions', __name__, url_prefix='/api/transaction')
session = Database.get_session()

@bp.before_request
def check_auth():
    session = request.cookies.get('session')
    if not session or not verify_token(session):
        return {"status": "unauthorized"}, 401

@bp.route('/create-wallet', methods=['GET'])
def create():
    _session = request.cookies.get('session')
    payload = jwt.decode(
        jwt=_session,
        options={"verify_signature": False}
    )
    user_id = payload.get('user_id')
    username = payload.get('username')
    if not user_id or not username:
        return {"status": "unauthorized"}, 401
    
    if TransactionService.safe_create_wallet(session, user_id, username):
        return {"status": "ok"}
    return {"status": "failed"}, 500

