from flask import Blueprint, request, jsonify
from server import db
from server.models import RestaurantPizza, Pizza, Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    errors = []
    if price is None or not (1 <= price <= 30):
        errors.append("Price must be between 1 and 30")
    if not pizza_id or not Pizza.query.get(pizza_id):
        errors.append("Pizza not found")
    if not restaurant_id or not Restaurant.query.get(restaurant_id):
        errors.append("Restaurant not found")
    if errors:
        return jsonify({"errors": errors}), 400

    try:
        rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(rp)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400

    return jsonify(rp.to_dict()), 201 