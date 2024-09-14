from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL) #connects you to database

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #Let's you talk to the database

Base = declarative_base() #All our models will extend this base class

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
