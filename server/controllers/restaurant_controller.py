"""
Controller for restaurant-related routes: GET, DELETE, and details with pizzas.
""" 

from flask import Blueprint, jsonify, request
from server import db
from server.models import Restaurant, Pizza, RestaurantPizza

restaurant_bp = Blueprint('restaurant_bp', __name__)

@restaurant_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants])

@restaurant_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    restaurant_data = restaurant.to_dict()
    pizzas_data = [rp.pizza.to_dict() for rp in restaurant.restaurant_pizzas]
    restaurant_data['pizzas'] = pizzas_data
    
    return jsonify(restaurant_data)

@restaurant_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204 