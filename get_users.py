from main import Session, Store_Database
from db_engine import engine

#First, let's bind the session to the engine.
local_session = Session(bind=engine)

# Then, let's get the info into a list of objects (or object of objects, I'm not sure)
users = local_session.query(Store_Database).all()

for user in users:
    print(user)

#If I wanted a specific user I would go like this:
#user = local_session.query(Store_Database).fileter(Store_Database.id==2).first()
