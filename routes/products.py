from flask import Blueprint, request, jsonify
from models.products import Products
from utils.db import db

products = Blueprint("products", __name__)

@products.route('/products', methods=['GET'])
def get_all_products():
    if request.method == 'GET':
        
        product = products.query.filter_by(id = id).first()

        if product is None:
            return jsonify(products = products.query.all())
        else:
            return jsonify(product = product)

@products.route('/products/<string:id>', methods=['GET'])
def get_product(id):
    if request.method == 'GET':

        product = products.query.filter_by(id = id).first()

        if product is None:
            return jsonify(product = product)
        else:
             return jsonify(products = products.query.all())

@products.route('/create', methods=['POST'])
def add_product():
    if request.method == 'POST':

        # receive data from the form
        quantity = request.get_json()['quantity']
        price = request.get_json()['price']

        # create a new product object
        new_product = Products(quantity, price, price)

        # save the object into the database
        db.session.add(new_product)
        db.session.commit()        

        return jsonify(message = 'created')


@products.route("/update/<string:id>", methods=["PUT"])
def update(id):
    # get product by Id
    print(id)
    product = product.query.get(id)

    if request.method == "PUT":
        product.quantity = request.get_json()['quantity']
        product.price = request.get_json()['price']

        db.session.commit()        

        return jsonify(message = 'updated')


@products.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    product = product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return jsonify(message = 'deleted')