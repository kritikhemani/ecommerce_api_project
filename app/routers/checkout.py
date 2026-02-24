from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db
from app.models.cart import Cart
from app.models.product import Product
from app.models.order import Order
from sqlalchemy import select
#from app.tasks.email import send_order_confirmation_email

router = APIRouter(prefix="/checkout", tags=["Checkout"])

@router.post("/")
async def checkout(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Cart).where(Cart.user_id == user_id))
    cart_items = result.scalars().all()
    total = 0
    for item in cart_items:
        product = await db.get(Product, item.product_id)
        total += product.price
    
    new_order = Order(user_id=user_id, total_price=total)
    db.add(new_order)
    
    for item in cart_items:
        await db.delete(item)
    await db.commit()
    
    