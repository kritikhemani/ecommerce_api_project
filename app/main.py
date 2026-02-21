from fastapi import FastAPI
from app.routers import products, cart

app = FastAPI(title="Ecommerce API")

@app.get("/")
async def home():
    return {"message": "Welcome to the Ecommerce API!"}

app.include_router(products.router)