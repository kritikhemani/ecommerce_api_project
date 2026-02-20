from pydantic import BaseModel, ConfigDict

class CreateProduct(BaseModel):
    name: str
    description: str
    price: float
    
class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    
    