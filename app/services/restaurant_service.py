from app.repositories.restaurant_repository import RestaurantRepository


class RestaurantService:

    def __init__(self):
        self.repository = RestaurantRepository()

    def create_restaurant(self, restaurant_data):
        return self.repository.create(restaurant_data)

    def get_restaurants(self):
        return self.repository.get_all()

    def get_restaurant(self, restaurant_id):
        return self.repository.get_by_id(restaurant_id)

    def update_restaurant(self, restaurant_id, restaurant_data):
        return self.repository.update(restaurant_id, restaurant_data)

    def delete_restaurant(self, restaurant_id):
        return self.repository.delete(restaurant_id)

    def filter_restaurants(self, city=None, category=None, price=None):
        restaurants = self.repository.get_all()

        if city:
            restaurants = [
                r for r in restaurants
                if r.get("city", "").lower() == city.lower()
            ]

        if category:
            restaurants = [
                r for r in restaurants
                if r.get("category", "").lower() == category.lower()
            ]

        if price:
            restaurants = [
                r for r in restaurants
                if r.get("price") == price
            ]

        return restaurants