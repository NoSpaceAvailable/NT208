from sqlalchemy import BigInteger, Boolean, Column, \
                        Date, DateTime, Enum, Float, ForeignKey, \
                        Integer, String, Text, Time, UniqueConstraint, func, and_, or_, Numeric
from sqlalchemy.orm import relationship
from . import BaseModel


class Items(BaseModel):
    """Store game items and its properties"""
    __tablename__ = 'items'

    id          = Column(Integer, primary_key=True, autoincrement=True)
    item_kind   = Column(String(32), nullable=False)
    item_name   = Column(String(32), nullable=False)
    item_type   = Column(String(32), nullable=False)
    rarity      = Column(String(1), nullable=False)      # describe the rarity of a product
    price       = Column(Integer, nullable=False)

    def __init__(self, item_kind, item_name, item_type, rarity, price):
        self.item_kind  = item_kind
        self.item_name  = item_name
        self.item_type  = item_type
        self.rarity     = rarity
        self.price      = price

    def to_dict(self):
        return {
            'id': self.id,
            'item_kind': self.item_kind,
            'item_name': self.item_name,
            'item_type': self.item_type,
            'rarity': self.rarity,
            'price': self.price
        }