from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int