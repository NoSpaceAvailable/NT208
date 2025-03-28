from sqlalchemy import BigInteger, Boolean, Column, \
                        Date, DateTime, Enum, Float, ForeignKey, \
                        Integer, String, Text, Time, UniqueConstraint, func, and_, or_
from sqlalchemy.orm import relationship
from . import BaseModel

class UserProfile(BaseModel):
    """Stores additional profile information for users."""
    __tablename__ = 'user_profiles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
    username = Column(String(32), ForeignKey('users.username'), nullable=False, unique=True)
    profile_name = Column(String(32), nullable=False, unique=True)
    bio = Column(Text, nullable=True)
    location = Column(String(128), nullable=True)
    birthdate = Column(Date, nullable=False)
    joined_at = Column(DateTime, server_default=func.now())
    wallet_address = Column(String(64), ForeignKey('wallets.wallet_address'), unique=True)

    user = relationship("User", back_populates="profile", foreign_keys=user_id)

    def __init__(self, user_id, username, profile_name, bio, location, birthdate, wallet_address):
        self.user_id = user_id
        self.username = username
        self.profile_name = profile_name
        self.bio = bio
        self.location = location
        self.birthdate = birthdate
        self.wallet_address = wallet_address

    def __repr__(self):
        return f"<UserProfile(id={self.id}, \
            user_id={self.user_id}, \
            bio='{self.bio}', \
            location='{self.location}', \
            birthdate={self.birthdate}, \
            wallet_address='{self.wallet_address}')>"