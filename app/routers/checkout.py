from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db

router = APIRouter(prefix="/checkout", tags=["Checkout"])

@router.post("/")
async def checkout():
    pass