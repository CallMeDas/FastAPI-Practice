
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from database import schemas
from database.database import products


load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

db_url = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost:5432/{DB_NAME}"
engine = create_engine(db_url)
session = sessionmaker(autoflush=False, autocommit= False, bind=engine)

Base = declarative_base()





class Product(Base):

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

def init_db():

    db = session()

    existing = db.query(Product).first()

    if existing:
        return

    for product in products:
        db.add(Product(**product.model_dump()))

    db.commit()
    db.close()


init_db()