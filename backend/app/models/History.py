from sqlalchemy import BigInteger, Boolean, Column, \
                        Date, DateTime, Enum, Float, ForeignKey, \
                        Integer, String, Text, Time, UniqueConstraint, func, and_, or_, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from .. global_config import history_config
from . import BaseModel
from hashlib import sha256

def generate_transaction_hash(
    sender_id: int,
    receiver_id: int,
    amount: float,
    timestamp: str,
    salt: bytes = history_config['TRANSACTION_SALT'],
) -> str:
    if sender_id <= 0 or receiver_id <= 0:
        raise ValueError("User IDs must be positive integers")
    if amount < 0:
        raise ValueError("Amount must be non-negative")
    if not isinstance(salt, bytes) or len(salt) != 4:
        raise ValueError("Salt must be 4 bytes")
    
    rounded_amount = round(amount, 2)
    transaction_string = f"{sender_id}{receiver_id}{rounded_amount:.2f}{timestamp}".encode("utf-8")
    
    return sha256(transaction_string + salt).hexdigest()

def get_current_time() -> str:
    local_time = datetime.now()
    utc_time = local_time.astimezone(timezone.utc)
    return utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")

class History(BaseModel):
    
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('user_profiles.user_id'), nullable=False)
    receiver_id = Column(Integer, ForeignKey('user_profiles.user_id'), nullable=False)
    amount = Column(Numeric(20, 2), nullable=False)
    timestamp = Column(String(24), default=get_current_time(), nullable=False)
    transaction_hash = Column(String(64), nullable=False, unique=True)
    reversed_hash = Column(String(64), nullable=True, unique=True)

    sender = relationship("UserProfile", foreign_keys=sender_id, back_populates="sent_transactions")

    def __init__(self, sender_id, receiver_id, amount):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.amount = amount
        self.timestamp = get_current_time()
        self.transaction_hash = generate_transaction_hash(sender_id, receiver_id, amount, self.timestamp)
        self.reversed_hash = generate_transaction_hash(receiver_id, sender_id, amount, self.timestamp)

    def get_hash(self):
        return self.transaction_hash
    
    def get_reversed_hash(self):
        return self.reversed_hash
    
    def __repr__(self):
        return f"<History(id={self.id}, \
            sender_id={self.sender_id}, \
            receiver_id={self.receiver_id}, \
            amount={self.amount}, \
            timestamp='{self.timestamp}', \
            transaction_hash='{self.transaction_hash}', \
            reversed_hash='{self.reversed_hash}')>"