from sqlalchemy import select, or_
from sqlalchemy.orm import Session
from .. models.History import History
from ..models.Wallet import Wallet
from ..models.User import User
from .. utils.logging import info, error
from .. global_config import history_config
from ..models.enumtypes.HistoryStatus import HistoryStatus
from ..models.enumtypes.HistoryType import HistoryType
from hashlib import sha256

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

class HistoryService:

    @staticmethod
    def select_one_by_transaction_hash(session: Session, transaction_hash: str) -> History | None:
        return session.execute(
            select(History)
            .filter(History.transaction_hash == transaction_hash)
        ).scalar_one_or_none()

    @staticmethod
    def safe_create_transaction_history(session: Session, 
                                        sender_address: str, 
                                        receiver_address: str, 
                                        amount: int, 
                                        timestamp: str,
                                        message: str, 
                                        status: HistoryStatus, 
                                        transaction_type: HistoryType):
        """
        Create two transaction history records in the database.
        """
        if amount <= 0:
            error("Invalid amount")
            return False
        try:
            transaction = History(sender_address, receiver_address, amount, timestamp, message, status, transaction_type)
            info(f"Creating transaction history: {transaction}")
            session.add(transaction)
            info(f"Transaction history added")
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            error(f"Failed to create transaction history: {e}")
            return False
        
    @staticmethod
    def safe_get_history_records(session: Session, username: str) -> History:
        """
        Retrieve a transaction history record by username.
        """
        _hash = session.execute(
            select(Wallet)
            .filter(
                Wallet.user_id == (
                    session.execute(
                        select(User.id)
                        .filter(User.username == username)
                    ).scalar_one_or_none()
                )
            ).with_for_update()
        ).scalar_one_or_none().wallet_address
        print(_hash, flush=True)
        try:
            records = session.execute(
                select(History)
                .filter(
                    or_(
                        History.sender_address == _hash,
                        History.receiver_address == _hash
                    ))
                .with_for_update()
            ).all()
            records = [record[0].to_dict() for record in records]
            print(records, flush=True)
            if records:
                info(f"Transaction history retrieved: {records}")
                return records
            else:
                error("Transaction not found")
                return None
        except Exception as e:
            error(f"Failed to retrieve transaction history: {e}")
            return None
