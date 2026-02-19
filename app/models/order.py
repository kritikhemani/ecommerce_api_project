from sqlalchemy import Column, Integer, Float
from app.database.connection import Base

class Order(Base):
    __tablename__ = 'orders'