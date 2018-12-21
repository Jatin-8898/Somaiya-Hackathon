from . import db
from flask_bcrypt import generate_password_hash
from flask_login import UserMixin

class User(UserMixin,db.Model):
    email = db.Column(db.String(100),primary_key=True)
    name = db.Column(db.String(50))
    credential = db.relationship('Credential',backref='user',uselist=False)

    def __init__(self,email,name):
        self.email = email
        self.name = name

    def get_id(self):
        return self.email


class Credential(db.Model):
    email = db.Column(db.String(100),db.ForeignKey('user.email'),primary_key=True)
    passCode = db.Column(db.String(60))

    def __init__(self,email,passCode):
        self.email = email
        self.passCode = generate_password_hash(passCode)


class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    category = db.Column(db.String(50))
    price = db.Column(db.Integer)
    reviews = db.relationship('Review',backref='product')

    def __init__(self,name,description,category,price):
        self.name = name
        self.description = description
        self.category = category
        self.price = price

class Media(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    image_path = db.Column(db.String(100))

    def __init__(self,image_path):
        self.image_path = image_path

class Review(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    product_id = db.Column(db.Integer,db.ForeignKey('product.id'))
    review_description = db.Column(db.String(150))
    date = db.Column(db.Date)
    rating = db.Column(db.Integer)

    def __init__(self,product_id,description,date,rating):
        self.product_id = product_id
        self.review_description = description
        self.date = date
        self.rating = rating