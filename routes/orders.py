from flask import Blueprint, request, jsonify
from models.orders import Orders
from utils.db import db
import datetime

orders = Blueprint("orders", __name__)

@orders.route('/orders', methods=['GET'])
def get_all_orders():
    if request.method == 'GET':
        
        order = Orders.query.filter_by(id = id).first()

        if order is None:
            return jsonify(orders = Orders.query.all())
        else:
            return jsonify(order = order)

@orders.route('/orders/<string:id>', methods=['GET'])
def get_order(id):
    if request.method == 'GET':

        order = Orders.query.filter_by(id = id).first()

        if order is None:
            return jsonify(order = order)
        else:
             return jsonify(orders = Orders.query.all())

@orders.route('/orders/create', methods=['POST'])
def add_order():
    if request.method == 'POST':

        # receive data from the form
        customer_id = request.get_json()['customer_id']
        product_id = request.get_json()['product_id']
        time = datetime.datetime()

        # create a new product object
        new_order = Orders(customer_id, product_id, time)

        # save the object into the database
        db.session.add(new_order)
        db.session.commit()        

        return jsonify(message = 'created')


@orders.route("/orders/update/<string:id>", methods=["PUT"])
def update(id):
    # get product by Id
    print(id)
    order = Orders.query.get(id)

    if request.method == "PUT":
        order.customer_id = request.get_json()['customer_id']
        order.product_id = request.get_json()['product_id']

        db.session.commit()        

        return jsonify(message = 'updated')


@orders.route("/orders/delete/<id>", methods=["DELETE"])
def delete(id):
    order = Orders.query.get(id)
    db.session.delete(order)
    db.session.commit()

    return jsonify(message = 'deleted')