import os
from app import app, db
from app.models import *
from flask import render_template


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/categories')
def categories():
    return render_template('categories.html')


@app.route('/<string:category>/<string:name>')
def single(category, name):
    product = Product.query.filter_by(
        category=category).filter_by(name=name).first()
    reviews = product.reviews
    return render_template('single.html', product=product, reviews=reviews)


@app.route('/payment')
def payment():
    return render_template('payment.html')


@app.route('/buy_token')
def buy_token():
    return render_template('buytokens.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
