from model import Session, User
from db_engine import engine

local_session = Session(bind=engine)

class UpdarteUser:
    def __init__(self):
        user_id = int(input("Type in the id of the user you wanna update: "))
        user = local_session.query(User).filter(User.id==user_id).first()
        user.username = input("Name of the user: ")
        user.email = input("Email of the user: ")
        local_session.commit()
