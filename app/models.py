from . import db

class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    category = db.Column(db.String(50))
    price = db.Column(db.Integer)
    reviews = db.relationship('Review',backref='product')

class Media(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    image_path = db.Column(db.String(100))

class Review(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    product_id = db.Column(db.Integer,db.ForeignKey('product.id'))
    review_description = db.Column(db.String(150))
    rating = db.Column(db.Integer)