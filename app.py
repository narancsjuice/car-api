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
# Run application
if __name__ == '__main__':
    app.run(debug=True)