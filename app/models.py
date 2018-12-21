from run import db


class Product(db.Model):
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    category = db.Column(db.Integer)
    price = db.Column(db.Integer)
