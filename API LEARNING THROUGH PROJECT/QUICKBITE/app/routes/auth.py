from flask import Blueprint, request, jsonify
import jwt, datetime
from flask import current_app
from ..models import User
auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data["username"]).first()

    if not user or user.password != data["password"]:
        return jsonify({"error": "Invalid credentials"}), 401

    token = jwt.encode(
        {"user_id": user.id},
        current_app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    return jsonify({"token": token})
