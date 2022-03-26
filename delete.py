from main import Session, Store_Database
from db_engine import engine

local_session = Session(bind=engine)

user_to_delete = local_session.query(Store_Database).filter(Store_Database.id==3).first()

#for user_to_delete in users_to_delete:
local_session.delete(user_to_delete)
local_session.commit()
