
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://admin:password@mymysqlinstance.cbyoyq0e6uzw.us-east-1.rds.amazonaws.com:3306/VictoriaProFitnessDb')    
Session = sessionmaker(bind=engine)
Base = declarative_base()