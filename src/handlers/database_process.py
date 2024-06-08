from datasources.mysql import Session, engine, Base
from models.database.user import User 
from utils.helpers import AlchemyEncoder
import json

def handler(event, context):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    session = Session()
    session.add(User(1,"user prueba"))
    s = json.dumps(session.query(User).all(), cls=AlchemyEncoder)
    
    session.commit()
    session.close()
        

    return s