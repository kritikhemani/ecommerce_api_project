from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db
from app.models.cart import Cart
from app.schemas.cart import CartCreate, CartResponse


router = APIRouter(prefix="/cart", tags=["Cart"])

@router.post("/", response_model=CartResponse)
async def add_to_cart(cart: CartCreate, db: AsyncSession = Depends(get_db)):
    pass