from app.core.firebase import db


class RestaurantRepository:

    COLLECTION = "restaurants"

    def create(self, restaurant_data):
        doc_ref = db.collection(self.COLLECTION).document()
        restaurant_data["id"] = doc_ref.id
        doc_ref.set(restaurant_data)
        return restaurant_data

    def get_all(self):
        restaurants = db.collection(self.COLLECTION).stream()
        return [
            {"id": restaurant.id, **restaurant.to_dict()}
            for restaurant in restaurants
        ]

    def get_by_id(self, restaurant_id):
        doc_ref = db.collection(self.COLLECTION).document(restaurant_id)
        restaurant = doc_ref.get()

        if not restaurant.exists:
            return None

        return {"id": restaurant.id, **restaurant.to_dict()}

    def update(self, restaurant_id, restaurant_data):
        doc_ref = db.collection(self.COLLECTION).document(restaurant_id)

        if not doc_ref.get().exists:
            return None

        doc_ref.update(restaurant_data)
        return self.get_by_id(restaurant_id)

    def delete(self, restaurant_id):
        doc_ref = db.collection(self.COLLECTION).document(restaurant_id)

        if not doc_ref.get().exists:
            return False

        doc_ref.delete()
        return True
