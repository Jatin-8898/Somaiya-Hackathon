from app import db
from app.models import *
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d")

db.drop_all()
db.create_all()

iphone = Product("IPhone","IPhone description","Phones",100)
laptop = Product("Laptop","Laptop description","Laptops",75)

iphone_review1 = Review(1,"Very Nice",date,4)
iphone_review2 = Review(1,"Ameeron ka phone hai yeh mat kharido",date,2)

db.session.add(iphone)
db.session.add(laptop)
db.session.add(iphone_review1)
db.session.add(iphone_review2)

db.session.commit()

