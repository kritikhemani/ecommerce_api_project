from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db
from models.product import Product
from app.schemas.product import CreateProduct, ProductResponse
from app.cache.redis import get_cache, set_cache


router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductResponse)
async def create_product(product: CreateProduct, db: AsyncSession = Depends(get_db)):
    pass