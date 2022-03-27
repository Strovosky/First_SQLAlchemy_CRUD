#Here, we'll create the interaction with user. So that they can run the CRUD from the terminal.

from create_users import CreateUser
from get_users import GetUsers
from update import UpdarteUser
from delete import DeleteUser

def intro():
    print("Welcome to the Contact Manager App.")
    print("For creating a new user, type C.")
    print("For reading all users, type RA.")
    print("For reading a specific user, type RU.")
    print("For updating a user a user, type U.")
    print("For deleting a user, type D.\n")
    print()

class ContactManager:
    def __init__(self):
        self.answer = input("Type in your command: ").upper()
        
        if self.answer == "C":
            CreateUser()
        elif self.answer == "RA":
            GetUsers().get_all_users()
        elif self.answer == "RU":
            GetUsers.get_user()
        elif self.answer == "U":
            UpdarteUser()
        else:
            DeleteUser()

        
    


if __name__ == "__main__":
    intro()
    ContactManager()




