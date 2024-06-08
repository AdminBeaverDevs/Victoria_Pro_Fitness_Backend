from datasources.mysql import Base
from sqlalchemy import Column, String, Integer, Date


class User(Base):
    __tablename__ = "User"
    UserId = Column(Integer,primary_key=True)
    Name = Column(String(100))
    
    def __init__(self, user_id, name):
        self.UserId = user_id
        self.Name = name
    