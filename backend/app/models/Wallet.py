from sqlalchemy import BigInteger, Boolean, Column, \
                        Date, DateTime, Enum, Float, ForeignKey, \
                        Integer, String, Text, Time, UniqueConstraint, func, and_, or_, Numeric
from sqlalchemy.orm import relationship
from . import BaseModel

class Wallet(BaseModel):

    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    wallet_address = Column(String(64), nullable=False, unique=True)
    balance = Column(Numeric(20, 2), default=0, nullable=False)
    
    owner = relationship("User", back_populates="wallet")

    def __init__(self, user_id, wallet_address):
        self.user_id = user_id
        self.wallet_address = wallet_address


    