from .extensions import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    item = db.Column(db.String(100))
    quantity = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "item": self.item,
            "quantity": self.quantity,
            "user": self.user.username
        }
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    orders = db.relationship("Order", backref="user", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }
