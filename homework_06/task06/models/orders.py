from pydantic import BaseModel, Field
from datetime import date


class OrderBillet(BaseModel):
    customer_id: int = Field(..., )
    good_id: int = Field(..., )
    order_date: date = Field(..., format="%Y-%m-%d")
    status: str = Field(..., )


class Order(OrderBillet):
    id: int
