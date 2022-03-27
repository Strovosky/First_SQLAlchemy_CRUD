# We import Session, cuz it's the one we use to create data into the database.
# We import the model Store_Dababase, cuz under this model we add info into the data base.
from model import Session, User

# We import engine cuz we need to bind the session with the database.
from db_engine import engine

#First, let's bind the session to the database.
local_session = Session(bind=engine)

class CreateUser:
    def __init__(self):
        user_name = input("Type in the user's name: ")
        user_email = input("Type in the user's email: ")
        
        user = User(username=user_name, email=user_email)

        local_session.add(user)
        local_session.commit()
