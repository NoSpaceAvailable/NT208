from sqlalchemy import BigInteger, Boolean, Column, \
                        Date, DateTime, Enum, Float, ForeignKey, \
                        Integer, String, Text, Time, UniqueConstraint, func, and_, or_
from sqlalchemy.orm import relationship
from . import BaseModel

class UserProfile(BaseModel):

    __tablename__ = 'user_profiles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    bio = Column(Text, nullable=True)
    location = Column(String(128), nullable=True)
    birthdate = Column(Date, nullable=False)
    joined_at = Column(DateTime, default=func.now())
    wallet_address = Column(String(128), nullable=False)

    def __init__(self, user_id, bio, location, birthdate, wallet_address):
        self.user_id = user_id
        self.bio = bio
        self.location = location
        self.birthdate = birthdate
        self.wallet_address = wallet_address

    def update(self, bio, location, birthdate, wallet_address):
        self.bio = bio
        self.location = location
        self.birthdate = birthdate
        self.wallet_address = wallet_address

    def get_profile(self):
        return {
            "bio": self.bio,
            "location": self.location,
            "birthdate": self.birthdate,
            "joined_at": self.joined_at,
            "wallet_address": self.wallet_address
        }

    def __repr__(self):
        return f"<UserProfile(id={self.id}, \
            user_id={self.user_id}, \
            bio='{self.bio}', \
            location='{self.location}', \
            birthdate={self.birthdate}, \
            wallet_address='{self.wallet_address}')>"