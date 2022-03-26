# We import Session, cuz it's the one we use to create data into the database.
# We import the model Store_Dababase, cuz under this model we add info into the data base.
from main import Session, Store_Database

# We import engine cuz we need to bind the session with the database.
from db_engine import engine

#First, let's bind the session to the database.
local_session = Session(bind=engine)

#Now, let's create the info we're going to put into the table we created.
new_users = [{
        "id": 1,
        "username": "Sara Hidalgo",
        "email": "saraflete@gmail.com"
    }, {
        "id": 2,
        "username": "Juan Carlos",
        "email": "juancarugby@gmail.com"
    }, 
    {
        "id": 3,
        "username": " Mariana Pato",
        "email": "patoaventuras@yahoo.com"
    }
]

for new_user in new_users:
    #Let's map the user according to the model Store_Database.
    user = Store_Database(id=new_user["id"], username=new_user["username"], email=new_user["email"])
    #Let's add this user into the session.
    local_session.add(user)
    #This one send the info to the database, like a commit in git.
    local_session.commit()

