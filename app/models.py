from . import db

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