from fastapi import HTTPException
from database.database import products
from database.schemas import Product



def get_all_products():
    return products


def get_product_by_id(product_id: int):

    for product in products:
        if product.id == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


def create_product(product: Product):

    for existing_product in products:
        if existing_product.id == product.id:
            raise HTTPException(
                status_code=400,
                detail="Product ID already exists"
            )

    products.append(product)
    return product


def update_product(product_id: int, updated_product: Product):

    for i in range(len(products)):

        if products[i].id == product_id:
            products[i] = updated_product
            return updated_product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


def delete_product(product_id: int):

    for i in range(len(products)):

        if products[i].id == product_id:
            deleted_product = products.pop(i)
            return deleted_product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )