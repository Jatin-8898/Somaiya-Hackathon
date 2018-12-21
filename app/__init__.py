from flask import Flask
from flask import render_template  
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)


app.config['SECRET_KEY'] = "sarvesh"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:sarvesh@localhost/ecommerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

