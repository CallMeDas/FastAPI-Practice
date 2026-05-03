from fastapi import HTTPException
# from database.database import products
from database.schemas import Product
from database.database_models import session
from fastapi import Depends
from database import database_models
from database.database_models import session

from sqlalchemy.orm import Session


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


def get_all_products(db: Session):
    db_products = db.query(database_models.Product).all()
    return db_products


def get_product_by_id(product_id: int,db: Session):

    db_product = db.query(database_models.Product).filter(
        database_models.Product.id == product_id
    ).first()
    if db_product:
        return Product
    else:
        return 'Product not Found.'



def create_product(product: Product, db: Session):

    existing_product = db.query(database_models.Product).filter(
        database_models.Product.id == product.id
    ).first()

    if existing_product:
        return 'Product ID already exists'

    db_product = database_models.Product(
        **product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(product_id: int, updated_product: Product,db: Session):
    db_product = db.query(database_models.Product).filter(
        database_models.Product.id == product_id
    ).first()

    if db_product:
        db_product.name = updated_product.name
        db_product.description = updated_product.description
        db_product.price = updated_product.price
        db_product.quantity = updated_product.quantity
        db.commit()
        return 'Product Updated.'
    else:
        return 'Product not found'


def delete_product(product_id: int, db: Session):

    product = db.query(database_models.Product).filter(
        database_models.Product.id == product_id
    ).first()

    if product:
        db.delete(product)
        db.commit()
        return 'Product Deleted.'
    else:
        return 'Product not found.'
