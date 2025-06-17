from server import db
from server.app import create_app
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()
app.app_context().push()

db.drop_all()
db.create_all()

r1 = Restaurant(name="Mario's Pizza", address="123 Main Street")
r2 = Restaurant(name="Luigi's Pizza", address="456 Side Avenue")

p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

db.session.add_all([r1, r2, p1, p2])
db.session.commit()

rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
rp2 = RestaurantPizza(price=12, pizza_id=p2.id, restaurant_id=r1.id)
rp3 = RestaurantPizza(price=8, pizza_id=p1.id, restaurant_id=r2.id)

db.session.add_all([rp1, rp2, rp3])
db.session.commit()

print("Database seeded!")
