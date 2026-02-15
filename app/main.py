from fastapi import FastAPI

app = FastAPI(title="Ecommerce API")

@app.get("/")
async def root():
    return {"message": "Welcome to the Ecommerce API!"}