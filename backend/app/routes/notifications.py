from flask import Blueprint, request
from ..services.notification_service import NotificationService
from ..models.Database import Database
from ..utils.cookie import verify_token
from ..services.profile_service import ProfileService
from functools import wraps
import json, jwt

bp = Blueprint('notifications', __name__, url_prefix='/api/notification')
db_session = Database.get_session()

def get_uid():
    session = request.cookies.get('session')
    return jwt.decode(session, options={"verify_signature": False}).get('user_id')

def user_created_profile(user_id) -> bool:
    user_id = get_uid()
    return ProfileService.safe_get_profile(db_session, user_id) is not None

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
    ret = NotificationService.get_notifications(session=db_session, user_id=user_id)
    return ret

@bp.route('/add', methods=['POST'])
@auth_required
def add():
    user_id = get_uid()
    data = request.json
    message = data['message']
    timestamp = None
    seen = False
    if not NotificationService.add_notification(session=db_session, user_id=user_id, message=message, timestamp=timestamp, seen=seen):
        return {'status': 'something went wrong'}, 400
    return {'status': 'notification added successfully'}

@bp.route('/mark/<notid>', methods=['GET'])
@auth_required
def mark(notid):
    user_id = get_uid()
    noti_id = notid
    if not NotificationService.update_seen(session=db_session, user_id=user_id, id=noti_id, new_seen=True):
        return {'status': 'something went wrong'}, 400
    return {'status': 'notification marked successfully'}