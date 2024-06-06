

from sqlalchemy import create_engine


def handler(event, context):
    cnx = create_engine('mysql+pymysql://admin:password@mymysqlinstance.cbyoyq0e6uzw.us-east-1.rds.amazonaws.com/VictoriaProFitnessDb')    
  
    return {}