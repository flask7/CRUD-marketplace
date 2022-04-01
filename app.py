from flask import Flask
from routes.products import products
from routes.orders import orders
from routes.customers import customers
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI
import os

app = Flask(__name__)

# settings
app.secret_key = os.urandom(32)
print(DATABASE_CONNECTION_URI)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

SQLAlchemy(app)

app.register_blueprint(products)
app.register_blueprint(orders)
app.register_blueprint(customers)
