from fastapi import FastAPI
from routes.product import router as product_router
from database import database_models
from database.database_models import engine

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

app.include_router(product_router)


@app.get("/")
def home():
    return {"message": "Working..."}