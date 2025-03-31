from sqlalchemy import BigInteger, Boolean, Column, \
                        Date, DateTime, Enum, Float, ForeignKey, \
                        Integer, String, Text, Time, UniqueConstraint, and_, or_
from sqlalchemy.orm import relationship
from datetime import datetime
from . import BaseModel

def reformat_date(date_str: str) -> str:
    """Reformat date string from yyyy-mm-dd to dd-mm-yyyy."""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d-%m-%Y")
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

class UserProfile(BaseModel):
    """Stores additional profile information for users."""
    __tablename__ = 'user_profiles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
    username = Column(String(32), ForeignKey('users.username'), nullable=False, unique=True)
    profile_name = Column(String(64), nullable=False, unique=True)
    full_name = Column(String(64), nullable=True, unique=False)
    bio = Column(String(256), nullable=True)
    location = Column(String(128), nullable=True)
    birthdate = Column(String(24), nullable=False)
    joined_at = Column(String(24), default=datetime.now().strftime("%d-%m-%Y"), nullable=False)
    wallet_address = Column(String(64), ForeignKey('wallets.wallet_address'), unique=True)

    user = relationship("User", back_populates="profile", foreign_keys=user_id)
    sent_transactions = relationship("History", foreign_keys="History.sender_id", back_populates="sender")

    def __init__(self, user_id, username, profile_name, full_name, bio, location, birthdate, wallet_address):
        self.user_id = user_id
        self.username = username
        self.profile_name = profile_name
        self.full_name = full_name
        self.bio = bio
        self.location = location
        self.birthdate = reformat_date(birthdate)
        self.wallet_address = wallet_address