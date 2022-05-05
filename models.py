from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import relationship

class Blogs(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key = True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer,ForeignKey("users.id"))
    creator = relationship("Users",back_populates = "blogs")

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key = True)
    name = Column(String)
    passwd = Column(String)
    email = Column(String)
    blogs = relationship("Blogs",back_populates = "creator")