from utils.db import db

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    house_type = db.Column(db.String)
    city = db.Column(db.String)

    def __init__(self, name, age, house_type, city):
        self.name = name
        self.age = age
        self.house_type = house_type
        self.city = city
