from main import Session, Store_Database
from db_engine import engine

local_session = Session(bind=engine)

#First, I should get the user, I will get it in an object that references the location on the database.
user_to_update = local_session.query(Store_Database).filter(Store_Database.id == 3).first()

#Then, I update the info in the object, which will also update the info in the database, becase the
# object references that location.
user_to_update.username = "Lalo"
user_to_update.email = "viajante@aol.com"
user_to_update.id = 3

#I commit the changes.
local_session.commit()

