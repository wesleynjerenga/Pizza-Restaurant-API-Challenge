from server import db, create_app
from server.models import Restaurant, Pizza, RestaurantPizza

def seed_database():
    app = create_app()
    with app.app_context():
        # Clear existing data
        RestaurantPizza.query.delete()
        Pizza.query.delete()
        Restaurant.query.delete()

        # Create restaurants
        restaurants = [
            Restaurant(name="Sottocasa NYC", address="298 Atlantic Ave, Brooklyn, NY 11201"),
            Restaurant(name="PizzArte", address="69 W 55th St, New York, NY 10019"),
            Restaurant(name="Joe's Pizza", address="7 Carmine St, New York, NY 10014")
        ]
        db.session.add_all(restaurants)
        db.session.commit()

        # Create pizzas
        pizzas = [
            Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese"),
            Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni"),
            Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Fresh Mozzarella, Basil"),
            Pizza(name="Vegetarian", ingredients="Dough, Tomato Sauce, Cheese, Bell Peppers, Mushrooms, Onions")
        ]
        db.session.add_all(pizzas)
        db.session.commit()

        # Create restaurant pizzas
        restaurant_pizzas = [
            RestaurantPizza(price=10, restaurant=restaurants[0], pizza=pizzas[0]),
            RestaurantPizza(price=12, restaurant=restaurants[0], pizza=pizzas[1]),
            RestaurantPizza(price=11, restaurant=restaurants[1], pizza=pizzas[2]),
            RestaurantPizza(price=13, restaurant=restaurants[1], pizza=pizzas[3]),
            RestaurantPizza(price=9, restaurant=restaurants[2], pizza=pizzas[0]),
            RestaurantPizza(price=11, restaurant=restaurants[2], pizza=pizzas[1])
        ]
        db.session.add_all(restaurant_pizzas)
        db.session.commit()

if __name__ == "__main__":
    seed_database()
    print("Database seeded successfully!") 