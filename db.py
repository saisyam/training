from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def create_db_string():
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    upass = os.getenv("DB_PASS")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_DATABASE")

    db_uri = 'postgresql://'+user+':'+upass+'@'+host+':'+port+'/'+db
    return db_uri
    

  

def create_session():
    db_uri = create_db_string()
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    return Session()

def close_session(s):
    s.close()