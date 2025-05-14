from sqlalchemy import select, and_, update
from sqlalchemy.orm import Session
from .. models import Items, UserItems
from .. models.enumtypes import ItemRarity
from .. utils.logging import info, error

class ProductService:

    @staticmethod
    def get_product_item(session: Session, item_type: str, rarity: str, item_name: str):
        item = session.execute(
            select(Items)
            .filter(and_(
                Items.item_type == item_type,
                Items.rarity == rarity,
                Items.item_name == item_name
            ))
        ).scalar_one_or_none()
        if not item:
            error(f"Not found for search: {item_type}, {rarity}, {item_name}", __name__)
        return item
    
    @staticmethod
    def get_inventory(session: Session, user_id: int):
        user_items = session.execute(
            select(UserItems)
            .filter(
                UserItems.user_id == user_id
            )
        ).all()
        inventory = [user_item[0].to_dict() for user_item in user_items]
        return inventory
    
    @staticmethod
    def item_is_belong_to(session: Session, user_item_id: int, user_id: int):
        record = session.execute(
            select(UserItems)
            .filter(and_(
                UserItems.id == user_item_id,
                UserItems.user_id == user_id
            ))
        ).scalar_one_or_none()
        return record != None
    
    @staticmethod
    def transfer_ownership_to(session: Session, user_item_id: int, new_user_id: int):
        """Must be used after item_is_belong_to()"""
        try:     
            session.execute(
                update(UserItems)
                .where(UserItems.id == user_item_id)
                .values(user_id = new_user_id)
            )
            session.flush()
            return True
        except Exception as e:
            error(f"Error while tranfering ownership: {e}", __name__)
            session.rollback()
            return False
        
    @staticmethod
    def update_sale_status(session: Session, user_item_id: int, new_sale_status: bool):
        """Must be used after item_is_belong_to()"""
        try:
            session.execute(
                update(UserItems)
                .where(UserItems.id == user_item_id)
                .values(for_sale=new_sale_status)
            )
            session.flush()
            return True
        except Exception as e:
            error(f"Error while changing sale status: {e}", __name__)
            session.rollback()
            return False
