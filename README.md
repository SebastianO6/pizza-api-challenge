 # Pizza Restaurant API
This is a simple RESTful API for a pizza restaurant built using Flask and SQLAlchemy. This project allows you to manage restaurants, pizzas, and the relationships between them through HTTP endpoints. No frontend is required.

# Features
Retrieve all restaurants

Retrieve details of a specific restaurant (with its pizzas)

Delete a restaurant and its related pizzas

Retrieve all pizzas

Create a restaurant-pizza relationship with price validation (1 to 30)

# Setup Instructions
Clone the repository and navigate to the project directory:

cd pizza-api
Create a virtual environment and install dependencies:

pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell

# Set up environment variables:

export FLASK_APP=server.app:create_app
Initialize the database:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Seed the database with initial data:

python -m server.seed

# Running the Application
# Start the Flask development server:
flask run
The API will be available at http://127.0.0.1:5000/.

# API Endpoints
Restaurants
GET /restaurants

Returns a list of all restaurants.

GET /restaurants/<id>

Returns details of a specific restaurant, including its pizzas.

Returns 404 if the restaurant does not exist.

DELETE /restaurants/<id>

Deletes a specific restaurant and all related restaurant-pizzas.

Returns 404 if the restaurant does not exist.

Returns 204 No Content on successful deletion.

Pizzas
GET /pizzas

Returns a list of all pizzas.

Restaurant Pizzas (Join Table)
POST /restaurant_pizzas

Creates a new RestaurantPizza with a specified price, pizza_id, and restaurant_id.


Price must be between 1 and 30, or a 400 error is returned.

Successful response includes related pizza and restaurant data.

Validation Rules
The price field in RestaurantPizza must be between 1 and 30.

Appropriate error messages and HTTP status codes are returned for invalid requests.

Database Migrations
To make future changes to the models:
flask db migrate -m "Your message"
flask db upgrade