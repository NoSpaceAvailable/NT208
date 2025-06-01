from sqlalchemy.ext.declarative import declarative_base
from app.models.Database import Database
db = Database()
engine = db._engine
BaseModel = declarative_base()

from .User import User
from .Wallet import Wallet
from .UserProfile import UserProfile
from .History import History
from .UserItems import UserItems
from .Items import Items
from .Notifications import Notifications

UserProfile.__table__.drop(engine, checkfirst=True)
Wallet.__table__.drop(engine, checkfirst=True)
UserItems.__table__.drop(engine, checkfirst=True)
Items.__table__.drop(engine, checkfirst=True)
Notifications.__table__.drop(engine, checkfirst=True)
User.__table__.drop(engine, checkfirst=True)
History.__table__.drop(engine, checkfirst=True)
        
BaseModel.metadata.create_all(engine)

conn = engine.raw_connection()
cursor = conn.cursor()
init = open('/app/app/misc/init.sql').read()
cursor.execute(init)
conn.commit()
conn.close()