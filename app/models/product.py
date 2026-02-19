from sqlalchemy import Column, Integer, String, Float
from app.database.connection import Base

class Product(Base):
    __tablename__ = 'products'