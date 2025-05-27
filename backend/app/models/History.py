from sqlalchemy import BigInteger, Boolean, Column, \
                        Date, DateTime, Enum, Float, ForeignKey, \
                        Integer, String, Text, Time, UniqueConstraint, func, and_, or_, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from .. global_config import history_config
from . import BaseModel
from hashlib import sha256
from .enumtypes.HistoryStatus import HistoryStatus

def generate_transaction_hash(
    sender_hash: str,
    receiver_hash: str,
    amount: int,
    timestamp: str,
    salt: bytes = history_config['TRANSACTION_SALT'],
) -> str:
    if len(sender_hash) != 64 or len(receiver_hash) != 64:
        raise ValueError("Sender and receiver hashes must be 64 characters long")
    if not isinstance(sender_hash, str) or not isinstance(receiver_hash, str):
        raise ValueError("Sender and receiver hashes must be strings")
    if amount < 0:
        raise ValueError("Amount must be non-negative")
    if not isinstance(salt, bytes) or len(salt) != 4:
        raise ValueError("Salt must be 4 bytes")
    
    transaction_string = f"{sender_hash}{receiver_hash}{amount}{timestamp}".encode("utf-8")
    
    return sha256(transaction_string + salt).hexdigest()

def get_current_time() -> str:
    local_time = datetime.now()
    utc_time = local_time.astimezone(timezone.utc)
    return utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")

class History(BaseModel):
    
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sender_address = Column(String(64), nullable=False)
    receiver_address = Column(String(64), nullable=False)
    amount = Column(Integer, nullable=False)
    timestamp = Column(String(24), default=get_current_time(), nullable=False)
    transaction_hash = Column(String(64), nullable=False, unique=True)
    message = Column(String(128), nullable=True)    # message from sender to receiver
    status = Column(String(6), nullable=False, default=HistoryStatus.PENDING.value)
    transaction_type = Column(String(16), nullable=False)

    def __init__(self, sender_address, receiver_address, amount, timestamp, message, status, transaction_type):
        self.sender_address = sender_address
        self.receiver_address = receiver_address
        self.amount = amount
        self.timestamp = timestamp
        self.transaction_hash = generate_transaction_hash(
            sender_hash=sender_address,
            receiver_hash=receiver_address,
            amount=amount,
            timestamp=timestamp
        )
        self.message = message
        self.status = status
        self.transaction_type = transaction_type
        
    def to_dict(self):
        return {
            'id': self.id,
            'sender_address': self.sender_address,
            'receiver_address': self.receiver_address,
            'amount': int(self.amount),
            'timestamp': self.timestamp,
            'transaction_hash': self.transaction_hash,
            'message': self.message,
            'status': self.status,
            'type': self.transaction_type
        }
    
    def set_status(self, status):
        if status not in HistoryStatus:
            raise ValueError("Invalid status")
        self.status = status
    
    def __repr__(self):
        return f"<History(id={self.id}, \
            sender_address={self.sender_address}, \
            receiver_address={self.receiver_address}, \
            amount={self.amount}, \
            timestamp='{self.timestamp}', \
            transaction_hash='{self.transaction_hash}', \
            message='{self.message}', \
            status='{self.status}', \
            type='{self.transaction_type}')>"