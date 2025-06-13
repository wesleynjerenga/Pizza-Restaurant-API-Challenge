# Pizza Restaurant API Challenge

A RESTful API for managing a pizza restaurant, built with Flask using the MVC (Model-View-Controller) pattern.

## Project Structure

```
.
├── server/
│   ├── __init__.py            # App factory and extension setup
│   ├── app.py                 # App entry point, registers controllers
│   ├── config.py              # Database and app configuration
│   ├── models/                # Data models (SQLAlchemy)
│   │   ├── __init__.py        # Imports all models
│   │   ├── restaurant.py      # Restaurant model
│   │   ├── pizza.py           # Pizza model
│   │   └── restaurant_pizza.py# Join model for Restaurant and Pizza
│   ├── controllers/           # Route handlers (Controllers)
│   │   ├── __init__.py        # Package marker
│   │   ├── restaurant_controller.py      # Restaurant routes
│   │   ├── pizza_controller.py           # Pizza routes
│   │   └── restaurant_pizza_controller.py# RestaurantPizza routes
│   ├── seed.py                # Script to seed the database
├── migrations/                # Database migration files (created by Flask-Migrate)
├── challenge-1-pizzas.postman_collection.json # Postman collection for testing
├── requirements.txt           # Python dependencies
├── .gitignore                 # Files and folders to ignore in git
├── test_app.py                # Placeholder for future tests
└── README.md                  # Project documentation
```

## What Each Part Does
- **server/config.py**: Sets up the database URI and Flask config.
- **server/__init__.py**: Initializes Flask app, SQLAlchemy, and Flask-Migrate.
- **server/app.py**: Entry point; creates app and registers all controllers (routes).
- **server/models/**: Contains SQLAlchemy models for Restaurant, Pizza, and RestaurantPizza (join table with price validation).
- **server/controllers/**: Contains route logic for each resource (restaurants, pizzas, restaurant_pizzas).
- **server/seed.py**: Seeds the database with sample data for testing.
- **migrations/**: Stores migration scripts for database schema changes.
- **challenge-1-pizzas.postman_collection.json**: Postman collection for API endpoint testing.
- **requirements.txt**: Lists required Python packages.
- **test_app.py**: Placeholder for future automated tests.

## Setup Instructions

1. **Clone the repository**
2. **Create and activate a virtual environment**
   ```bash
   pipenv install
   pipenv shell
   ```
3. **Install dependencies**
   ```bash
   pipenv install flask flask_sqlalchemy flask_migrate
   ```
4. **Set up the database**
   ```bash
   export FLASK_APP=server/app.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
5. **Seed the database**
   ```bash
   python server/seed.py
   ```

## API Routes

### Restaurants
- `GET /restaurants`: List all restaurants
- `GET /restaurants/<id>`: Get a restaurant and its pizzas
- `DELETE /restaurants/<id>`: Delete a restaurant and its related RestaurantPizzas

### Pizzas
- `GET /pizzas`: List all pizzas

### Restaurant Pizzas
- `POST /restaurant_pizzas`: Create a new RestaurantPizza (join with price validation)

## Example Requests & Responses

**POST /restaurant_pizzas**
Request:
```json
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```
Success Response:
```json
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3,
  "pizza": { "id": 1, "name": "Emma", "ingredients": "Dough, Tomato Sauce, Cheese" },
  "restaurant": { "id": 3, "name": "Kiki's Pizza", "address": "address3" }
}
```
Error Response:
```json
{ "errors": ["Price must be between 1 and 30"] }
```

## Validation Rules
- RestaurantPizza price must be between 1 and 30
- All required fields must be present in requests
- Restaurant and Pizza IDs must exist in the database

## Testing with Postman
1. Import the provided Postman collection: `challenge-1-pizzas.postman_collection.json`
2. Run the Flask server
3. Use the collection to test all endpoints

## Contribution & License
Feel free to fork and contribute. See LICENSE for details.