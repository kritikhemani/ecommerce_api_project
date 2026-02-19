from sqlalchemy import Column, Integer, ForeignKey
from app.database.connection import Base

class Cart(Base):
    __tablename__ = 'cart'