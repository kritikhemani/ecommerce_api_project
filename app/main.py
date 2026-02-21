from fastapi import FastAPI
from app.routers import products, cart

app = FastAPI(title="Ecommerce API")

@app.get("/")
async def root():
    return {"message": "Welcome to the Ecommerce API!"}