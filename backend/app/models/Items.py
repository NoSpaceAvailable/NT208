from sqlalchemy import BigInteger, Boolean, Column, \
                        Date, DateTime, Enum, Float, ForeignKey, \
                        Integer, String, Text, Time, UniqueConstraint, func, and_, or_
from sqlalchemy.orm import relationship
from . import BaseModel


class Items(BaseModel):
    """Store game items and its properties"""
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    rarity = Column(String(6), nullable=False)      # describe the rarity of a product
    skin_name = Column(String(32), nullable=False)
    price = Column(Integer, nullable=False)
    image_path = Column(String(64), nullable=False) # path to image on local system 