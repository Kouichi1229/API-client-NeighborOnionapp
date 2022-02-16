import datetime
from pydantic import BaseModel, Field

class BookingCreate(BaseModel):
    p_id: int
    a_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime
    
class Booking(BookingCreate):
    booking_id: int

    class Config:
        orm_mode = True
    
class UserCreate(BaseModel):
    temp: str = Field(max_length=300)
    rain: str = Field(max_length=300)
    

class User(UserCreate):
    p_id: int

    class Config:
        orm_mode = True

class RoomCreate(BaseModel):
    aler: str = Field(min_length=12,max_length=500)
    
    

class Room(RoomCreate):
    a_id: int

    class Config:
        orm_mode = True


