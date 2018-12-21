from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_oauthlib.client import OAuth
from flask_login import LoginManager


pymysql.install_as_MySQLdb()

app = Flask(__name__)


app.config['SECRET_KEY'] = "sarvesh"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://Jatin8898:kingjatin@localhost/ecommerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login = LoginManager(app)

oauth = OAuth(app)

google = oauth.remote_app('google',
    base_url="https://www.googleapis.com/oauth2/v3",
    consumer_key="241334067780-n4plv2si1tc3k42oeag2naembmm8vm86.apps.googleusercontent.com",
    consumer_secret="ofW6HaRHlF1-EdyMygsJY1ur",
    request_token_params={
        "scope": "email"
    },
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://www.googleapis.com/oauth2/v3/token',
    authorize_url="https://accounts.google.com/o/oauth2/auth"
)

db = SQLAlchemy(app)

from app.models import User

@login.user_loader
def load_user(email):
    return User.query.filter_by(email=email).first()
