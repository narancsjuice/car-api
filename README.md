# car-api
**Preview 0.1**

This is a basic Python API example built with Flask, SQLAlchemy and Marshmallow.

Its functions include:
- adding new cars to the database
- updating cars in the database
- querying cars by id or all cars from the database
- deleting cars in the database

To query the API the following JSON format is used:
```{
    "manufacturer": "Nissan",
    "type": "GTR",
    "year": 2017,
    "description": "black, brand new GTR",
    "price": 65000
}
```

To run this project you need Python 3.9 installed. Also, please check the 
requirements.txt to install the necessary Python libraries.

