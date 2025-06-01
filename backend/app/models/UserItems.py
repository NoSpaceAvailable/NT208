from sqlalchemy import BigInteger, Boolean, Column, \
                        Date, DateTime, Enum, Float, ForeignKey, \
                        Integer, String, Text, Time, UniqueConstraint, func, and_, or_, select
from sqlalchemy.orm import relationship
from app.models import BaseModel
from app.models.Database import Database    
from app.models.Items import Items
from app.models.enumtypes import ItemCollection, ItemExterior
import random

session = Database.get_session()
foo = [e.value for e in ItemExterior.ItemExterior]
bar = [e.value for e in ItemCollection.ItemCollection]
STATTRAK_RATE = 7 # %

def random_collection():
    return [random.choice(foo), (True if random.randint(0, 100) < STATTRAK_RATE else False), random.choice(bar)]

class UserItems(BaseModel):
    """Show ownership of users to game items"""
    __tablename__ = 'user_items'

    id      = Column(Integer, primary_key=True, autoincrement=True)         # will use this to track ownership
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)       # must be an existing user
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)       # must be an existing item

    item_exterior   = Column(String(32), nullable=False)
    item_stattrak   = Column(Boolean, nullable=False, default=False)
    item_collection = Column(String(64), nullable=True, default='No collection')

    for_sale        = Column(Boolean, nullable=False, default=False)

    def __init__(self, user_id, item_id, for_sale=False):
        random_set = random_collection()
        self.user_id = user_id
        self.item_id = item_id
        self.item_exterior = random_set[0]
        self.item_stattrak = random_set[1]
        self.item_collection = random_set[2]
        self.for_sale=for_sale

    def to_dict(self):
        item_record = session.execute(
            select(Items)
            .filter(
                Items.id == self.item_id
            )
        ).scalar_one_or_none()
        if item_record:
            return {
                'id': self.id,
                'item': item_record.to_dict(),
                'properties': {
                    'exterior': self.item_exterior,
                    'stattrak': self.item_stattrak,
                    'collection': self.item_collection,
                    'for_sale': self.for_sale,
                }
            }
        else:
            return None