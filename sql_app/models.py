from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql.functions import user
from sqlalchemy.sql.sqltypes import Date
from .database import Base

class User(Base):
    __tablename__ = 'users'
    
    p_id = Column(Integer, primary_key=True, index=True)
    temp = Column(String)
    rain = Column(String)
    #time = Column(DateTime, nullable=False)

class Room(Base):
    __tablename__ = 'rooms'

    a_id = Column(Integer, primary_key=True, index=True)
    aler = Column(String, unique=True, index=True)
    #time = Column(DateTime, nullable=False)

class Booking(Base):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True, index=True)
    p_id = Column(Integer, ForeignKey('users.p_id', ondelete='SET NULL'), nullable=False)
    a_id = Column(Integer, ForeignKey('rooms.a_id', ondelete='SET NULL'), nullable=False)
    booked_num = Column(Integer)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)

