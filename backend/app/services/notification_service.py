from sqlalchemy import select, and_, update, insert, func
from sqlalchemy.orm import Session
from .. models import Notifications
from .. utils.logging import info, error
from ..utils.timing import *

class NotificationService:

    @staticmethod
    def get_notifications(session: Session, user_id: int):
        try:
            notices = session.execute(
                select(Notifications)
                .filter(
                    Notifications.user_id == user_id
                )
            ).all()
            notifications = [notice[0].to_dict() for notice in notices]
            return notifications
        except Exception as e:
            error(f"Error while fetching user notifications: {e}", __name__)
            session.rollback()
            return []
    
    @staticmethod
    def add_notification(session: Session, user_id: int, message: str, timestamp: str = get_current_time(), seen: bool = False):
        try:
            new_notification = Notifications(
                user_id=user_id,
                message=message,
                timestamp=timestamp,
                seen=seen
            )
            session.add(new_notification)
            session.commit()
            return True
        except Exception as e:
            error(f"Error while adding notification: {e}", __name__)
            session.rollback()
            return False
        
    @staticmethod
    def update_seen(session: Session, user_id: int, id: int, new_seen: bool):
        try:
            session.execute(
                update(Notifications)
                .where(Notifications.user_id == user_id)
                .where(Notifications.id == id)
                .values(seen = new_seen)
            )
            session.flush()
            return True
        except Exception as e:
            error(f"Error while editing notification: {e}", __name__)
            session.rollback()
            return False