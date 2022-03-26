from main import Session, Store_Database
from db_engine import engine
from sqlalchemy import desc #I import this one if I wanna order the info in descending order.

local_session = Session(bind=engine)

#Ordering Results In Ascending Order
users = local_session.query(Store_Database).order_by(Store_Database.username).all()

for user in users:
    print(user)

#Ordering Results in Descending Order
#users = local_session.query(Store_Database).order_by(desc(Store_Database.username)).all()

