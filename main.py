from fastapi import FastAPI
from models import Product

app = FastAPI()


@app.get("/")
def greet():
    return 'Hello'


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


@app.get('/product')
def get_all_products():
    return products

@app.get('/product/{id}')
def get_all_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return 'no product found'


@app.post('/product')
def add_product(product: Product):
    products.append(product)
    return product


@app.put('/product')
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "uptaed sucessfuly"
    return "no product found"

@app.delete('/product')
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return 'product deleted'
    return 'product not found'
