from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db
from app.models.product import Product
from app.schemas.product import CreateProduct, ProductResponse
from app.cache.redis import get_cache, set_cache
from sqlalchemy import select
from typing import List


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
    cache_key = f"product:{product_id}"
    cache = get_cache(cache_key)
    if cache:
        print("Cache hit")
        return cache
    print("Cache miss")
    
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product_data = ProductResponse.from_orm(product).dict()
    set_cache(cache_key, product_data)
    return product_data

@router.get("/", response_model=List[ProductResponse])
async def list_products(db: AsyncSession = Depends(get_db)):
    cache_key = "all_products"
    cached_products = get_cache(cache_key)
    if cached_products:
        print("Cache hit for all products")
        return cached_products
    print("Cache miss for all products")
    result = await db.execute(select(Product))
    products = result.scalars().all()
    product_list = [ProductResponse.from_orm(product) for product in products]
    set_cache(cache_key, product_list, expire=60) 
    return product_list