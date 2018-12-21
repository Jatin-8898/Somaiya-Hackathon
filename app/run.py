import os
from flask import Flask
from flask import render_template  
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)


app.config['SECRET_KEY'] = "sarvesh"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://Jatin-8898:kingjatin@localhost/ecommerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/categories')
def categories():
    return render_template('categories.html')


@app.route('/single')
def single():
    return render_template('single.html')


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
