from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db


router = APIRouter(prefix="/products", tags=["Products"])