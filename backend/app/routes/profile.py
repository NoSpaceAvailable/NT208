from flask import Blueprint, request
from .. services.transaction_service import *
from .. utils.cookie import verify_token
from .. models.Database import Database
from .. services.profile_service import ProfileService
import jwt

bp = Blueprint('profile', __name__, url_prefix='/api/profile')
session = Database.get_session()

def get_uid():
    session = request.cookies.get('session')
    return jwt.decode(session, options={"verify_signature": False}).get('user_id')

def user_created_profile(user_id) -> bool:
    user_id = get_uid()
    return ProfileService.safe_get_profile(session, user_id) is not None

@bp.before_request
def check_auth():
    session = request.cookies.get('session')
    if not session or not verify_token(session):
        return {"status": "unauthorized"}, 401
    
@bp.route('/exist', methods=['GET'])
def exists():
    """Check if a profile exists for the current user."""
    user_id = get_uid()
    if user_created_profile(user_id):
        return { "status": "ok" }, 200
    return { "status": "error" }, 404

@bp.route('/create', methods=['POST'])
def create():
    """Create a profile for the current user."""
    user_id = get_uid()
    if user_created_profile(user_id):
        return { "status": "error" }, 404
    profile = request.json
    if ProfileService.safe_create_profile(session, user_id, profile):
        session.commit()
        return { "status": "ok" }, 200
    return { "status": "error", "msg": "please submit enough and valid infomation!" }, 500
    
@bp.route('/fetch/<uid>', methods=['GET'])
def profile(uid):
    """Fetch the user profile. This is publicly available for everyone to view"""
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
