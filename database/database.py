from database.schemas import Product
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

db_url = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost:5432/{DB_NAME}"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autoflush=False, autocommit= False, bind=engine)

products = [
    Product(id=1, name="Watch", description="Good to wear", price=890, quantity=30),
    Product(id=2, name="Laptop", description="Powerful performance", price=55000, quantity=10),
    Product(id=3, name="Phone", description="Latest smartphone", price=25000, quantity=20),
    Product(id=4, name="Headphones", description="Noise cancelling", price=3500, quantity=15),
    Product(id=5, name="Keyboard", description="Mechanical keyboard", price=2200, quantity=25),
    Product(id=6, name="Mouse", description="Wireless mouse", price=1200, quantity=40),
    Product(id=7, name="Shoes", description="Comfortable running shoes", price=4500, quantity=18),
    Product(id=8, name="Bag", description="Stylish backpack", price=2800, quantity=12),
    Product(id=9, name="Camera", description="High resolution camera", price=72000, quantity=5),
    Product(id=10, name="Tablet", description="Portable and lightweight", price=18000, quantity=8),
]