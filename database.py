from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///database/tables.db")

Base = declarative_base()

session = Session(bind = engine,expire_on_commit = False)

def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()