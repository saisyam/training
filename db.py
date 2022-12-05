from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

def create_db_string():
    host = os.getenv("PG_HOST")
    user = os.getenv("PG_USER")
    upass = os.getenv("PG_PASS")
    port = os.getenv("PG_PORT")
    db = os.getenv("PG_DB")

    db_uri = 'postgresql://'+user+':'+upass+'@'+host+':'+port+'/'+db
    return db_uri

def create_session():
    db_uri = create_db_string()
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    return Session()

def close_session(s):
    s.close()

