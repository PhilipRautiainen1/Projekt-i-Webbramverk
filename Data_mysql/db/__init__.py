import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .settings import *

engine = sqlalchemy.create_engine(f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


