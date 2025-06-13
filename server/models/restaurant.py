from server import db

"""
Restaurant model: represents a restaurant entity with name, address, and related pizzas.
"""

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    # Relationships
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete-orphan')  # Cascade delete

    def to_dict(self):
        # Serialize restaurant without pizzas
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }

    def to_dict_with_pizzas(self):
        # Serialize restaurant with related pizzas
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'pizzas': [rp.pizza.to_dict() for rp in self.restaurant_pizzas]
        } 