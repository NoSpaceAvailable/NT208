from sqlalchemy import BigInteger, Boolean, Column, \
                        Date, DateTime, Enum, Float, ForeignKey, \
                        Integer, String, Text, Time, UniqueConstraint, func, and_, or_
from sqlalchemy.orm import relationship
from . import BaseModel
import bcrypt

class User(BaseModel):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    reputation = Column(Integer, default=0)
    is_oauth2 = Column(Boolean, default=False)

    wallet = relationship("Wallet", uselist=False, back_populates="owner")
    profile = relationship("UserProfile", uselist=False, back_populates="user", foreign_keys="UserProfile.user_id")

    def __init__(self, username, email, password, reputation=0, is_oauth2=False):
        self.username = username
        self.email = email
        self.set_password(password, is_oauth2=is_oauth2)
        self.reputation = reputation
        self.is_oauth2 = is_oauth2

    def set_password(self, password, is_oauth2=False):
        """Hash the password and store it."""
        # Generate a salt and hash the password
        if is_oauth2:
            self.password_hash = "1337" # Placeholder for OAuth2 users
            return
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def check_password(self, password):
        """Verify the provided password against the hashed password."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def __repr__(self):
        return f"<User(id={self.id}, \
            username='{self.username}', \
            email='{self.email}', \
            reputation={self.reputation})>"