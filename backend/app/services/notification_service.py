from sqlalchemy import select, and_, update, insert, func
from sqlalchemy.orm import Session
from .. models import Notifications
from ..models.Database import Database
from .. utils.logging import info, error

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
            notifications = [notice.to_dict() for notice in notices]
            return notifications
        except Exception as e:
            error(f"Error while fetching user notifications: {e}", __name__)
            session.rollback()
            return []
    
    def add_notification(session: Session, user_id: int, message: str, timestamp: str, seen: bool = False):
        try:
            max_id = session.query(func.max(Notifications.id)).scalar()
            next_id = (max_id or 0) + 1

            new_notification = Notifications(
                id=next_id,
                user_id=user_id,
                message=message,
                timestamp=timestamp,
                seen=seen
            )
            session.execute(
                insert(Notifications)
                .values(new_notification)
                .on_conflict_do_nothing(index_elements=['id'])
            )
            session.flush()
            return True
        except Exception as e:
            error(f"Error while adding notification: {e}", __name__)
            session.rollback()
            return False
        
    @staticmethod
    def update_seen(session: Session, user_id: int, id: int, new_seen: bool):
        """Must be used after item_is_belong_to()"""
        try:
            session.execute(
                update(Notifications)
                .where(Notifications.user_id == user_id and Notifications.id == id)
                .values(seen = new_seen)
            )
            session.flush()
            return True
        except Exception as e:
            error(f"Error while editing notification: {e}", __name__)
            session.rollback()
            return False
