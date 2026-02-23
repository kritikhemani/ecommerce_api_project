from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db
from app.models.cart import Cart


router = APIRouter(prefix="/cart", tags=["Cart"])