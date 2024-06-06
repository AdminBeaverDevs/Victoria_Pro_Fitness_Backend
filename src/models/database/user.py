import sqlalchemy.ext.declarative.declarative_base

base = declarative_base()

class User(base):
    __tablename__ = "User"
    ShipName = Column(String,primary_key=True)
    Freight = Column(String)