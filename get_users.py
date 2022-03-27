from model import Session, User
from db_engine import engine

#First, let's bind the session to the engine.
local_session = Session(bind=engine)

class GetUsers:
    def get_all_users(self):
        users = local_session.query(User).all()
        for user in users:
            print(user)
    
    def get_user(self):
        user_id = int(input("Type in the user's id: "))
        try:
            user = local_session.query(User).filter(User.id==user_id).first()
            print(user)
        except:
            print("This user does not exist.")


#If I wanted a specific user I would go like this:
#user = local_session.query(Store_Database).fileter(Store_Database.id==2).first()
