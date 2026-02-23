from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db
from models.product import Product
from app.schemas.product import CreateProduct, ProductResponse


router = APIRouter(prefix="/products", tags=["Products"])