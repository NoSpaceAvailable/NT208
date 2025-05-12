from sqlalchemy import select, and_
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