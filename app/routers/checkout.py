from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/checkout", tags=["Checkout"])

@router.post("/")
async def checkout():
    pass