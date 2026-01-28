from flask import jsonify

def register_error_handlers(app):  # <-- receives Flask instance

    @app.errorhandler(400)
    def bad_request(error):
        print("DEBUG: 400 Bad Request triggered")
        return jsonify({"error": "Bad Request"}), 400

    @app.errorhandler(404)
    def not_found(error):
        print("DEBUG: 404 Not Found triggered")
        return jsonify({"error": "Resource Not Found"}), 404

    @app.errorhandler(500)
    def server_error(error):
        print("DEBUG: 500 Server Error triggered")
        return jsonify({"error": "Internal Server Error"}), 500
