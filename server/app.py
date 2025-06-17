from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizza_restaurant.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    restaurant_data = restaurant.to_dict()
    restaurant_data['pizzas'] = [rp.pizza.to_dict() for rp in restaurant.restaurant_pizzas]
    
    return jsonify(restaurant_data)

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    db.session.delete(restaurant)
    db.session.commit()
    
    return '', 204

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([pizza.to_dict() for pizza in pizzas])

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
    price = data.get('price')
    if not isinstance(price, int) or not 1 <= price <= 30:
        return jsonify({"errors": ["Price must be an integer between 1 and 30"]}), 400
    
    if not all(key in data for key in ['price', 'pizza_id', 'restaurant_id']):
        return jsonify({"errors": ["Missing required fields"]}), 400
    
    pizza = Pizza.query.get(data['pizza_id'])
    restaurant = Restaurant.query.get(data['restaurant_id'])
    
    if not pizza or not restaurant:
        return jsonify({"errors": ["Pizza or Restaurant not found"]}), 400
    
    restaurant_pizza = RestaurantPizza(
        price=data['price'],
        pizza_id=data['pizza_id'],
        restaurant_id=data['restaurant_id']
    )
    
    db.session.add(restaurant_pizza)
    db.session.commit()
    
    return jsonify({
        "id": restaurant_pizza.id,
        "price": restaurant_pizza.price,
        "pizza": pizza.to_dict(),
        "restaurant": restaurant.to_dict()
    }), 201

if __name__ == "__main__":
    app.run(port=5555, debug=True)