from flask import Blueprint, jsonify
from server.models import Pizza

pizza_bp = Blueprint('pizzas', __name__)

"""
Controller for pizza-related routes: GET all pizzas.
"""

@pizza_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([p.to_dict() for p in pizzas]) 