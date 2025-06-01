from flask import Blueprint, request
from app.services.transaction_service import *
from app.utils.cookie import verify_token
from app.models.Database import Database
from app.services.profile_service import ProfileService
import jwt
from functools import wraps

bp = Blueprint('profile', __name__, url_prefix='/api/profile')

def get_session():
    return Database.get_session()

def get_uid():
    session = request.cookies.get('session')
    return jwt.decode(session, options={"verify_signature": False}).get('user_id')

def user_created_profile(user_id) -> bool:
    session = get_session()
    try:
        user_id = get_uid()
        return ProfileService.safe_get_profile(session, user_id) is not None
    finally:
        session.close()

def auth_required(f):
    @wraps(f)
    def check_auth(*args, **kwargs):
        session = request.cookies.get('session')
        if not session or not verify_token(session):
            return {'status': 'unauthorized'}, 401
        return f(*args, **kwargs)
    return check_auth
    
@bp.route('/exist', methods=['GET'])
@auth_required
def exists():
    """Check if a profile exists for the current user."""
    user_id = get_uid()
    session = get_session()
    try:
        if user_created_profile(user_id):
            return { "status": "ok" }, 200
        return { "status": "error" }, 404
    finally:
        session.close()

@bp.route('/create', methods=['POST'])
@auth_required
def create():
    """Create a profile for the current user."""
    user_id = get_uid()
    session = get_session()
    try:
        if user_created_profile(user_id):
            return { "status": "error" }, 404
        profile = request.json
        if ProfileService.safe_create_profile(session, user_id, profile):
            session.commit()
            return { "status": "ok" }, 200
        return { "status": "error", "msg": "please submit enough and valid infomation!" }, 500
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
    
@bp.route('/fetch/<uid>', methods=['GET'])
def profile(uid):
    """Fetch the user profile. This is publicly available for everyone to view"""
    session = get_session()
    try:
        if uid == 'me':
            user_id = get_uid()
        elif uid == 'all':
            user_id = -1
        else:
            try:
                user_id = int(uid)
            except:
                return { "status": "error" }, 404
        profile = ProfileService.get_profile_for_display(session, user_id)
        if not profile:
            return { "status": "error" }, 404
        return { "status": "success", "profile": profile }, 200
    finally:
        session.close()
