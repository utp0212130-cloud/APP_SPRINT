from fastapi import APIRouter, HTTPException, Query

from app.domain.schemas import RestaurantCreate, RestaurantUpdate
from app.services.restaurant_service import RestaurantService


router = APIRouter(prefix="/api/v1/restaurants", tags=["Restaurants"])

service = RestaurantService()


@router.post("/")
def create_restaurant(restaurant: RestaurantCreate):
    return service.create_restaurant(restaurant.model_dump())


@router.get("/")
def get_restaurants(
    city: str = None,
    category: str = None,
    price: int = Query(default=None, ge=1, le=4)
):
    return service.filter_restaurants(city, category, price)


@router.get("/{restaurant_id}")
def get_restaurant(restaurant_id: str):
    restaurant = service.get_restaurant(restaurant_id)

    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")

    return restaurant


@router.put("/{restaurant_id}")
def update_restaurant(restaurant_id: str, restaurant: RestaurantUpdate):
    updated = service.update_restaurant(
        restaurant_id,
        restaurant.model_dump()
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")

    return updated


@router.delete("/{restaurant_id}")
def delete_restaurant(restaurant_id: str):
    deleted = service.delete_restaurant(restaurant_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")

    return {"message": "Restaurante eliminado correctamente"}