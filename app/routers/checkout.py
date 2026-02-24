from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db
from app.models.cart import Cart
from app.models.product import Product
from app.models.order import Order

router = APIRouter(prefix="/checkout", tags=["Checkout"])

@router.post("/")
async def checkout(user_id: int, db: AsyncSession = Depends(get_db)):
    pass