from flask import Blueprint, request, jsonify, abort
from ..models import Order
from ..extensions import db
from ..utils.auth import token_required

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/orders", methods=["POST"])
@token_required
def create_order():
    data = request.get_json()

    order = Order(
        item=data["item"],
        quantity=data["quantity"],
        user_id=request.user_id
    )

    db.session.add(order)
    db.session.commit()

    return jsonify(order.to_dict()), 201
