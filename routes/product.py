from fastapi import APIRouter, Depends
from database.schemas import Product
from core import crud
from sqlalchemy.orm import Session
from core.crud import get_db

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return crud.get_all_products(db)


@router.get("/{product_id}")
def get_product(product_id: int):
    return crud.get_product_by_id(product_id)


@router.post("/")
def add_product(product: Product, db: Session = Depends(get_db)):
    return crud.create_product(product,db)


@router.put("/{product_id}")
def update_product(product_id: int, product: Product,db: Session = Depends(get_db)):
    return crud.update_product(product_id, product,db)


@router.delete("/{product_id}")
def delete_product(product_id: int,db: Session = Depends(get_db)):
    return crud.delete_product(product_id,db)