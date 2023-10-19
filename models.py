from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    quantity = db.Column(db.Integer, default=0)

    def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity
