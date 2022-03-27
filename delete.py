from model import Session, User
from db_engine import engine

local_session = Session(bind=engine)

class DeleteUser:
    def __init__(self):
        user_id = int(input("Type in the id of the user to delete: "))
        user_to_delete = local_session.query(User).filter(User.id==user_id).first()
        local_session.delete(user_to_delete)
        local_session.commit()
