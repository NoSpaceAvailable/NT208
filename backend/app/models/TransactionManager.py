from sqlalchemy import BigInteger, Boolean, Column, \
                        Date, DateTime, Enum, Float, ForeignKey, \
                        Integer, String, Text, Time, UniqueConstraint, func, and_, or_
from sqlalchemy.orm import relationship
from hashlib import sha256
from .. global_config import history_config
from . import BaseModel

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


class TransactionManager(BaseModel):

    __tablename__ = 'transaction_manager'

    id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_hash = Column(String(64), ForeignKey('history.transaction_hash'), nullable=False)
    transaction_type = Column(String(16), nullable=False)
    status = Column(String(6), nullable=False)
    