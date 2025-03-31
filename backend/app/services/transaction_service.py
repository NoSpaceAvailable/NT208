from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from .. models import Wallet
from .. services.user_service import UserService
from .. services.history_service import HistoryService
from hashlib import sha256
from .. utils.logging import info, error

class TransactionService:
    @staticmethod
    def generate_wallet_address(username: str) -> str:
        return sha256(username.encode()).hexdigest()
    
    @staticmethod
    def safe_create_wallet(session: Session, user_id: int, username: str) -> str | bool:
        try:
            address = TransactionService.generate_wallet_address(username)
            wallet = Wallet(
                user_id=user_id, 
                wallet_address=address
            )
            session.add(wallet)
            session.commit()
            info(f"Wallet {address} created for user {username}.", __name__)
            return address
        except SQLAlchemyError as e:
            error(f"Failed to create wallet for {username}: {str(e)}", __name__)
            session.rollback()
            return False
        
    @staticmethod
    def _get_locked_wallet(session: Session, wallet_address: str) -> Wallet:
        """Internal method to get wallet with lock."""
        wallet = session.execute(
            select(Wallet)
            .filter(Wallet.wallet_address == wallet_address)
            .with_for_update()
        ).scalar_one_or_none()
        
        if not wallet:
            raise ValueError(f"Wallet {wallet_address} not found")
        return wallet

    @staticmethod
    def safe_add(session: Session, wallet_address: str, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive!")
            
        try:
            wallet = TransactionService._get_locked_wallet(session, wallet_address)
            wallet.balance += amount
            info(f"Added {amount} to wallet {wallet_address}. New balance: {wallet.balance}", __name__)
        except Exception as e:
            error(f"Failed to add to {wallet_address}, reason: {str(e)}", __name__)
            session.rollback()
            raise
        
    @staticmethod
    def safe_sub(session: Session, wallet_address: str, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        try:
            wallet = TransactionService._get_locked_wallet(session, wallet_address)
            if wallet.balance < amount:
                raise ValueError(f"Insufficient funds. Balance: {wallet.balance}, Attempted: {amount}")
            wallet.balance -= amount
            info(f"Subtracted {amount} from {wallet_address}. New balance: {wallet.balance}", __name__)
        except Exception as e:
            error(f"Failed to subtract from {wallet_address}, reason: {str(e)}", __name__)
            session.rollback()
            raise
        
    @staticmethod
    def safe_transaction(session: Session, sender_id: int, receiver_address: str, amount: float) -> bool:

        if amount <= 0:
            error("Amount must be positive", __name__)
            return False
        
        sender_address = UserService.get_wallet_address(session=session, user_id=sender_id)
        if not sender_address:
            error(f"Sender wallet address not found for user {sender_id}", __name__)
            return False

        if sender_address == receiver_address:
            error("Sender and receiver cannot be the same", __name__)
            return False
            
        try:
            TransactionService.safe_sub(session, sender_address, amount)
            TransactionService.safe_add(session, receiver_address, amount)
            session.commit()
            info(f"Transferred {amount} from {sender_address} to {receiver_address}", __name__)
            return True
        except Exception as e:
            error(f"Transfer failed from {sender_address} to {receiver_address}, reason: {str(e)}", __name__)
            session.rollback()
            return False
        
    @staticmethod
    def safe_get_balance(session: Session, username: str) -> float | None:

        wallet_address = sha256(username.encode()).hexdigest()
        try:
            wallet = TransactionService._get_locked_wallet(session, wallet_address)
            if not wallet:
                raise ValueError(f"Wallet {wallet_address} not found")
            info(f"Retrieved balance for {wallet_address}: {wallet.balance}", __name__)
            return wallet.balance
        except SQLAlchemyError as e:
            error(f"Failed to get balance for {wallet_address}: {str(e)}", __name__)
            return None