from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db
from app.models.product import Product
from app.schemas.product import CreateProduct, ProductResponse
from app.cache.redis import get_cache, set_cache
from sqlalchemy import select


router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductResponse)
async def create_product(product: CreateProduct, db: AsyncSession = Depends(get_db)):
    new_product = Product(name=product.name, description=product.description, price=product.price)
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    pass