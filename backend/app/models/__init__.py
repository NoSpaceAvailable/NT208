from sqlalchemy.ext.declarative import declarative_base
from .Database import Database

db = Database()
engine = db._engine
BaseModel = declarative_base()

from .User import User
from .Wallet import Wallet
from .UserProfile import UserProfile
from .History import History

History.__table__.drop(engine, checkfirst=True)
UserProfile.__table__.drop(engine, checkfirst=True)
Wallet.__table__.drop(engine, checkfirst=True)
User.__table__.drop(engine, checkfirst=True)

BaseModel.metadata.create_all(engine)