from fastapi import FastAPI
from routes.product import router as product_router

app = FastAPI()

app.include_router(product_router)


@app.get("/")
def home():
    return {"message": "Working..."}