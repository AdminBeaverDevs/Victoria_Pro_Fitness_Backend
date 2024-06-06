

from sqlalchemy import create_engine
from models.database.user import User 
from sqlalchemy.orm import sessionmaker


def handler(event, context):
    
    engine = create_engine('mysql+pymysql://admin:password@mymysqlinstance.cbyoyq0e6uzw.us-east-1.rds.amazonaws.com/VictoriaProFitnessDb')    
    Session = sessionmaker(bind=engine)    
    db_conn.create(User)
    return {}