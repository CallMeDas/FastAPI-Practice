from fastapi import APIRouter
from database.schemas import Product
from core import crud

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/")
def get_products():
    return crud.get_all_products()


@router.get("/{product_id}")
def get_product(product_id: int):
    return crud.get_product_by_id(product_id)


@router.post("/")
def add_product(product: Product):
    return crud.create_product(product)


@router.put("/{product_id}")
def update_product(product_id: int, product: Product):
    return crud.update_product(product_id, product)


@router.delete("/{product_id}")
def delete_product(product_id: int):
    return crud.delete_product(product_id)