import os
from app import app, db, google
from app.models import *
from flask import render_template, url_for, request, json, redirect
from flask_login import login_user, login_required, LoginManager,  logout_user, current_user
import requests
import json


@app.route('/')
def index():
    return render_template('home.html', current_user=current_user)


@app.route('/categories')
def categories():
    return render_template('categories.html')


@app.route('/<string:category>/<string:name>')
def single(category, name):
    product = Product.query.filter_by(
        category=category).filter_by(name=name).first()
    reviews = product.reviews
    #return product.name
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


@app.route("/googleLogin")
def googleLogin():
    return google.authorize(callback=url_for('.authorised', _external=True))


@app.route("/authorised")
def authorised():
    resp = google.authorized_response()
    authorizationHeader = {
        "Authorization": resp['token_type']+" "+resp['access_token']}
    response = requests.get(google.base_url+"/userinfo",
                            headers=authorizationHeader)
    response = json.loads(response.text)
    user = User.query.get(response['email'])
    if user is None:
        user = User(response['email'], response['name'])
        db.session.add(user)
    login_user(user)
    return redirect(url_for('.index'))  # .index requires func


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
