from datetime import datetime


class Restaurant:
    def __init__(
        self,
        id: str,
        name: str,
        category: str,
        city: str,
        price: int,
        description: str = "",
        address: str = "",
        created_at=None
    ):
        self.id = id
        self.name = name
        self.category = category
        self.city = city
        self.price = price
        self.description = description
        self.address = address
        self.created_at = created_at or datetime.now()