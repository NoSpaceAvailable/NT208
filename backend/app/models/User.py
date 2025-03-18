from sqlalchemy import BigInteger, Boolean, Column, \
                        Date, DateTime, Enum, Float, ForeignKey, \
                        Integer, String, Text, Time, UniqueConstraint, func, and_, or_
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .Database import Database
import bcrypt

db = Database()
engine = db._engine
Base = declarative_base()

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    reputation = Column(Integer, default=0)

    def __init__(self, username, email, password, reputation=0):
        self.username = username
        self.email = email
        self.set_password(password)
        self.reputation = reputation

    def set_password(self, password):
        """Hash the password and store it."""
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def check_password(self, password):
        """Verify the provided password against the hashed password."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}', reputation={self.reputation})>"
    
User.__table__.drop(engine, checkfirst=True)    
Base.metadata.create_all(engine)