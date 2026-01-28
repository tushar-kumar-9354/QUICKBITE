from flask import Blueprint, jsonify, request


from flask import Blueprint, jsonify, render_template

health_bp = Blueprint("health", __name__)

@health_bp.route("/", methods=["GET"])
def health():
    print("DEBUG: Health check endpoint hit")

    # API-style response
    if "application/json" in str(request.headers):
        return jsonify({
            "status": "OK",
            "message": "QuickBite API is running"
        })

    # Browser-style response
    return render_template("index.html")
