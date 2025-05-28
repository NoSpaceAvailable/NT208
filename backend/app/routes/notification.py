from flask import Blueprint, request
from ..services.notification_service import NotificationService
from ..models.Database import Database
from ..utils.cookie import verify_token
from ..services.profile_service import ProfileService
from functools import wraps
import json, jwt

bp = Blueprint('notifications', __name__, url_prefix='/api/notification')

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

@bp.route('/read', methods=['GET'])
@auth_required
def show_user_notification():
    user_id = get_uid()
    session = get_session()
    try:
        ret = NotificationService.get_notifications(session=session, user_id=user_id)
        return ret
    finally:
        session.close()

@bp.route('/mark/<notid>', methods=['GET'])
@auth_required
def mark(notid):
    user_id = get_uid()
    session = get_session()
    try:
        noti_id = notid
        if not NotificationService.update_seen(session=session, user_id=user_id, id=noti_id, new_seen=True):
            return {'status': 'something went wrong'}, 400
        session.commit()
        return {'status': 'notification marked successfully'}
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()