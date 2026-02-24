from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db
from app.models.cart import Cart
from app.models.product import Product
from app.models.order import Order

router = APIRouter(prefix="/checkout", tags=["Checkout"])

@router.post("/")
async def checkout():
    pass