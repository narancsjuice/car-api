from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize application
app = Flask(__name__)
dbdir = os.path.abspath(os.path.dirname(__file__))

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dbdir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)


# Car Model
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String(100))
    type = db.Column(db.String(100))
    year = db.Column(db.Integer)
    description = db.Column(db.String(250))
    price = db.Column(db.Integer)

    def __init__(self, manufacturer, type, year, description, price):
        self.manufacturer = manufacturer
        self.type = type
        self.year = year
        self.description = description
        self.price = price


# Car Schema
class CarSchema(ma.Schema):
    class Meta:
        fields = ('id', 'manufacturer', 'type', 'year', 'description', 'price')


# Initialize Schema
car_schema = CarSchema()
cars_schema = CarSchema(many=True)


# Create car
@app.route('/car', methods=['POST'])
def add_car():
    manufacturer = request.json['manufacturer']
    type = request.json['type']
    year = request.json['year']
    description = request.json['description']
    price = request.json['price']

    new_car = Car(manufacturer, type, year, description, price)
    db.session.add(new_car)
    db.session.commit()

    return car_schema.jsonify(new_car)


# Get all cars
@app.route('/cars', methods=['GET'])
def get_cars():
    all_cars = Car.query.all()
    result = cars_schema.dump(all_cars)

    return jsonify(result)


# Get car by id
@app.route('/car/<id>', methods=['GET'])
def get_car(id):
    car = Car.query.get(id)

    return car_schema.jsonify(car)


# Update car
@app.route('/car/<id>', methods=['PUT'])
def update_car(id):
    car = Car.query.get(id)
    manufacturer = request.json['manufacturer']
    type = request.json['type']
    year = request.json['year']
    description = request.json['description']
    price = request.json['price']

    car.manufacturer = manufacturer
    car.type = type
    car.year = year
    car.description = description
    car.price = price

    db.session.commit()

    return car_schema.jsonify(car)


# Delete car by id
@app.route('/car/<id>', methods=['DELETE'])
def delete_car(id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()

    return "Deleted car id [" + str(car.id) +"]"


# Run application
if __name__ == '__main__':
    app.run(debug=True)