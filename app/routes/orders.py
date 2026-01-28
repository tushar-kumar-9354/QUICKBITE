from flask import Blueprint, request, jsonify, abort
from ..models import Order
from ..extensions import db
from ..utils.auth import token_required

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")

@orders_bp.route("/", methods=["GET"])
@token_required
def get_orders():
    orders = Order.query.filter_by(user_id=request.user_id).all()
    return jsonify([o.to_dict() for o in orders])

@orders_bp.route("/", methods=["POST"])  # ADD THIS: Create new order
@token_required
def create_order():
    data = request.get_json()
    
    # Validate required fields
    if not data or "item" not in data or "quantity" not in data:
        return jsonify({"error": "Missing item or quantity"}), 400
    
    try:
        quantity = int(data["quantity"])
        if quantity <= 0:
            return jsonify({"error": "Quantity must be positive"}), 400
    except ValueError:
        return jsonify({"error": "Quantity must be a number"}), 400
    
    # Create new order
    new_order = Order(
        user_id=request.user_id,
        item=data["item"],
        quantity=quantity
    )
    
    db.session.add(new_order)
    db.session.commit()
    
    return jsonify({
        "message": "Order created successfully",
        "order": new_order.to_dict()
    }), 201