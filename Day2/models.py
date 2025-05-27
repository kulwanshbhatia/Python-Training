# this class will represent Table in database

from sqlalchemy import Column,String
from .database import Base

class UserApp(Base):
    __tablename__="USERAPP"

    uname=Column(String,primary_key=True)
    email=Column(String)
    city=Column(String)
    