

from sqlalchemy import create_engine
from models.database.user import User 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase


def handler(event, context):
    
    engine = create_engine('mysql+pymysql://admin:password@mymysqlinstance.cbyoyq0e6uzw.us-east-1.rds.amazonaws.com:3306/VictoriaProFitnessDb')    
    Session = sessionmaker(bind=engine)    
    Base = DeclarativeBase()
    Base.metadata.create_all(engine)

    return {}