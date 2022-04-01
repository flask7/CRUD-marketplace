from utils.db import db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    quantity = db.Column(db.Float(16))
    price = db.Column(db.Float(16))

    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
