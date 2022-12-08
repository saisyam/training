from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import psycopg2
from dotenv import load_dotenv
from conf import *

load_dotenv()

def create_db_string():
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_DATABASE")

    db_uri = 'postgresql://'+user+':'+password+'@'+host+':'+port+'/'+database
    return db_uri
    

def create_session():
    db_uri = create_db_string()
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    return Session()

def close_session(s):
    s.close()