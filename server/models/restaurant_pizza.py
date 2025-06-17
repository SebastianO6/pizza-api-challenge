from .. import db

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    
    def __repr__(self):
        return f'<RestaurantPizza ${self.price}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'pizza': self.pizza.to_dict(),
            'restaurant': self.restaurant.to_dict()
        }
    
    @staticmethod
    def validate_price(price):
        if not isinstance(price, int) or not 1 <= price <= 30:
            raise ValueError("Price must be an integer between 1 and 30")