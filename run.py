import os
from app import app,db
from app.models import *
from flask import render_template

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/categories')
def categories():
    return render_template('categories.html')


@app.route('/<string:category>/<string:name>')
def single(category,name):
    product = Product.query.filter_by(category=category).filter_by(name=name).first()
    #return product.name
    return render_template('single.html',product=product)


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
