from pydantic import BaseModel, ConfigDict

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_price: float
    model_config = ConfigDict(from_attributes=True)