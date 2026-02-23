from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db
from app.models.cart import Cart
from app.schemas.cart import CreateCart, CartResponse


router = APIRouter(prefix="/cart", tags=["Cart"])