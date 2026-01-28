from .extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)  # Or password_hash if you changed it
    
    orders = db.relationship("Order", backref="user", lazy=True)
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)  # MUST EXIST
    item = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    
    def to_dict(self):
        return {
            "id": self.id,
            "item": self.item,
            "quantity": self.quantity,
            "user": self.user.username if self.user else None
        }