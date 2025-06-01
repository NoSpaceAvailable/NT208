from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import UserProfile, Wallet, User
from app.utils.logging import info, error

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
    
    @staticmethod
    def get_user_id(session: Session, username_or_waller_addr: str):
        if len(username_or_waller_addr) == 64:
            return session.query(UserProfile).filter(UserProfile.wallet_address == username_or_waller_addr).first().user_id
        return session.query(User).filter(User.username == username_or_waller_addr).first().id
    
    @staticmethod
    def get_wallet_address(session: Session, user_id: int | str) -> str:
        if isinstance(user_id, int):
            address = session.execute(
                select(Wallet.wallet_address)
                .filter(Wallet.user_id == user_id)
                .with_for_update()
            ).scalar_one_or_none()
            if not address:
                error(f"Wallet address for user {user_id} not found.", __name__)
                return None
            return address
        else:
            _user_id = UserService.get_user_id(session, user_id)
            return UserService.get_wallet_address(session, _user_id)