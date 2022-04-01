from crypt import methods
import json
from flask import Blueprint, request, jsonify
from models.customers import Customers
from utils.db import db

customers = Blueprint("customers", __name__)

@customers.route('/customers', methods=['GET'])
def get_all_customers():
    if request.method == 'GET':
        
        customer = Customers.query.filter_by(id = id).first()

        if customer is None:
            return jsonify(customers = Customers.query.all())
        else:
            return jsonify(customer = customer)

@customers.route('/customers/<string:id>', methods=['GET'])
def get_customer(id):
    if request.method == 'GET':

        customer = Customers.query.filter_by(id = id).first()

        if customer is None:
            return jsonify(customer = customer)
        else:
             return jsonify(customers = Customers.query.all())

@customers.route('/customers/create', methods=['POST'])
def add_customer():
    if request.method == 'POST':

        # receive data from the form
        name = request.get_json()['name']
        age = request.get_json()['age']
        house_type = request.get_json()['house_type']
        city = request.get_json()['house_type']

        # create a new customer object
        new_customer = Customers(name, age, house_type, city)

        # save the object into the database
        db.session.add(new_customer)
        db.session.commit()        

        return jsonify(message = 'created')


@customers.route("/customers/update/<string:id>", methods=["PUT"])
def update(id):
    # get product by Id
    print(id)
    customer = customers.query.get(id)

    if request.method == "PUT":
        customer.name = request.get_json()['name']
        customer.age = request.get_json()['age']
        customer.house_type = request.get_json()['house_type']
        customer.city = request.get_json()['house_type']

        db.session.commit()        

        return jsonify(message = 'updated')


@customers.route("/customers/delete/<id>", methods=["DELETE"])
def delete(id):
    customer = customers.query.get(id)
    db.session.delete(customer)
    db.session.commit()

    return jsonify(message = 'deleted')