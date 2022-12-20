import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

load_dotenv()

def create_db_string():
    database = os.getenv('database')
    host=os.getenv('host')
    user=os.getenv('user')
    password=os.getenv('password')
    port=os.getenv('port')
    engine_url="postgresql://"+user+":"+password+"@"+host+":"+port+"/"+database
    return engine_url

def create_session():
    engine_url = create_db_string()
    engine = create_engine(engine_url)
    Session = sessionmaker(bind=engine,expire_on_commit=False)
    return Session()

def authentication():
    TOKEN=os.getenv('token')
    headers = {
    'Authorization': 'token '+TOKEN}
    return headers

def close_session(s):
    s.close()
