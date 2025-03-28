from sqlalchemy import select
from sqlalchemy.orm import Session
from .. models import User
from .. utils.logging import info, error

class UserService:
    @staticmethod
    def safe_get_user(session: Session, user_id: int) -> User:
        user = session.execute(
            select(User)
            .filter(User.id == user_id)
            .with_for_update()
        ).scalar_one_or_none()
        if not user:
            error(f"User {user_id} not found.", __name__)
            return None
        return user