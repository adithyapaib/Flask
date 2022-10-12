""" Imports """
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId
from pymongo import MongoClient
from bson.json_util import dumps
import string, secrets, datetime, pika, json
alphabet = string.ascii_letters + string.digits


app = Flask(__name__)
CORS(app)
client = MongoClient('localhost', 27017)
db = client.pizza_house
collection = db.orders


""" Routes """
@app.route('/welcome', methods=['GET'])
def welcome():
    return jsonify({'message': 'Welcome to Pizza House'}), 200, {'ContentType': 'application/json'}

@app.route('/order', methods=['POST'])
def addorder():
    order = request.get_json()
    if not order:
        return jsonify({'message': 'No order data provided'}), 400, {'ContentType': 'application/json'}
    id = db.orders.insert_one(order)
    return jsonify({'order_id': str(id.inserted_id)}), 200, {'ContentType': 'application/json'}

@app.route('/getorders', methods=['GET'])
def getorders():
    orders = db.orders.find()
    return dumps(orders), 200, {'ContentType': 'application/json'}


@app.route('/getorders/<order_id>', methods=['GET'])
def getorder(order_id):
    if not ObjectId.is_valid(order_id):
        return jsonify({'message': 'Invalid order id'}), 400, {'ContentType': 'application/json'}
    order = db.orders.find_one({'_id': ObjectId(order_id)})
    if not order:
        return jsonify({'message': 'No order found'}), 404, {'ContentType': 'application/json'}
    return dumps(order), 200, {'ContentType': 'application/json'}


""" Order queue """
@app.route('/order_queue', methods=['POST'])
def addorder_queue():
    order = request.get_json()
    if not order:
        return jsonify({'message': 'No order data provided'}), 400, {'ContentType': 'application/json'}
    id = db.orders.insert_one(order)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='order_queue')
    channel.basic_publish(exchange='', routing_key='order_queue', body=str(id.inserted_id))
    connection.close()
    return jsonify({'message': 'Order added successfully', 'order_id': str(id.inserted_id)}), 200, {'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run(debug=True, port=5000)
