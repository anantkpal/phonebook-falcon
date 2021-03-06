from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import SETTINGS
engine = create_engine(SETTINGS['DB_URL'])
Session = sessionmaker(bind=engine)

Base = declarative_base()
