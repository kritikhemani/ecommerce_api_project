from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(prefix="/products", tags=["Products"])