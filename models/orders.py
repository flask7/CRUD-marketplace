from utils.db import db

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    quantity = db.Column(db.Float(16))

    def __init__(self, customer_id, product_id, time, quantity):
        self.customer_id = customer_id
        self.product_id = product_id
        self.time = time
        self.quantity = quantity
