from sqlalchemy import BigInteger, Boolean, Column, \
                        Date, DateTime, Enum, Float, ForeignKey, \
                        Integer, String, Text, Time, UniqueConstraint, func, and_, or_, Numeric
from sqlalchemy.orm import relationship
from . import BaseModel

class Notifications(BaseModel):
    """Store user notifications"""
    __tablename__ = 'notifications'
    id          = Column(Integer, primary_key=True, autoincrement=True)
    user_id     = Column(Integer, ForeignKey('users.id'), nullable=False)
    message     = Column(String(256), nullable=False)
    timestamp   = Column(String(64), nullable=False)
    seen        = Column(Boolean, default=False, nullable=False)

    def __init__(self, user_id, message, timestamp=None, seen=False):
        self.user_id = user_id
        self.message = message
        self.timestamp = timestamp or func.now()
        self.seen = seen

    def to_dict(self):
        return {
            'id': self.id,
            'message': self.message,
            'timestamp': self.timestamp.strftime("%H:%M:%S %d-%m-%Y foo bar"),
            'seen': self.seen
        }