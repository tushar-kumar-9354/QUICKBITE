from flask import request, abort
import jwt
from functools import wraps
from flask import current_app
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization", "").split(" ")[-1]

        data = jwt.decode(
            token,
            current_app.config["SECRET_KEY"],
            algorithms=["HS256"]
        )

        request.user_id = data["user_id"]
        return f(*args, **kwargs)
    return decorated
