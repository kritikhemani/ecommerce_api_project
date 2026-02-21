from pydantic import BaseModel, ConfigDict

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_amount: float
    model_config = ConfigDict(from_attributes=True)