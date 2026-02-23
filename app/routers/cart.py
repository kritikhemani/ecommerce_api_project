from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db
from app.models.cart import Cart
from app.schemas.cart import CartCreate, CartResponse
from sqlalchemy import select


router = APIRouter(prefix="/cart", tags=["Cart"])

@router.post("/", response_model=CartResponse)
async def add_to_cart(cart: CartCreate, db: AsyncSession = Depends(get_db)):
    new_cart = Cart(user_id=cart.user_id, product_id=cart.product_id)
    db.add(new_cart)
    await db.commit()
    await db.refresh(new_cart)
    return new_cart

@router.get("/{cart_id}", response_model=CartResponse)
async def get_cart(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Cart))
    carts = result.scalars().all()
    return carts