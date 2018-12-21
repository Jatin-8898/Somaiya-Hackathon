from app import db
from app.models import *

db.drop_all()
db.create_all()
