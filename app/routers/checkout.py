from fastapi import APIRouter

router = APIRouter(prefix="/checkout", tags=["Checkout"])

@router.post("/")
async def checkout():
    pass