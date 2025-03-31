from sqlalchemy import select, or_
from sqlalchemy.orm import Session
from .. models.History import History
from .. utils.logging import info, error
from .. global_config import history_config
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

class HistoryService:

    @staticmethod
    def safe_create_transaction_history(session: Session, sender_id: int, receiver_id: int, amount: float):
        """
        Create two transaction history records in the database.
        """
        if sender_id <= 0 or receiver_id <= 0:
            error("Invalid sender or receiver ID")
            return False
        if amount <= 0:
            error("Invalid amount")
            return False
        try:
            transaction = History(sender_id, receiver_id, amount)
            info(f"Creating transaction history: {transaction}")
            session.add(transaction)
            info(f"Transaction history added")
            return True
        except Exception as e:
            session.rollback()
            error(f"Failed to create transaction history: {e}")
            return False
        
    @staticmethod
    def safe_get_history_record(session: Session, _hash: str) -> History:
        """
        Retrieve a transaction history record by its hash.
        """
        try:
            record = session.execute(
                select(History)
                .filter(
                    or_(
                        History.transaction_hash == _hash,
                        History.reversed_hash == _hash
                    ))
                .with_for_update()
            ).scalar_one_or_none()

            if record:
                info(f"Transaction history retrieved: {record}")
                return record
            else:
                error("Transaction not found")
                return None
        except Exception as e:
            error(f"Failed to retrieve transaction history: {e}")
            return None
