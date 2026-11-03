from pydantic import BaseModel, Field


class RestaurantCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    category: str
    city: str
    price: int = Field(..., ge=1, le=4)
    description: str = ""
    address: str = ""


class RestaurantUpdate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    category: str
    city: str
    price: int = Field(..., ge=1, le=4)
    description: str = ""
    address: str = ""