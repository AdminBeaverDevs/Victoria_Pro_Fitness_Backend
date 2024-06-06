from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "User"
    ShipName = Column(String,primary_key=True)
    Freight = Column(String)