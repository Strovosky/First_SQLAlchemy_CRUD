# Let's create the table.

# First, we create the declarative_base and pass it to the class table we'll create.
# Then, we'll create the table schema. That is, how we want the table to be.

from datetime import datetime  # To work with a datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

Session = sessionmaker()

# Necessary to create the table model.
Base = declarative_base()

class Store_Database(Base):
    __tablename__= "Users1"  # This will create the table name.
    id = Column(Integer(), primary_key=True) # This is the primary key.
    username = Column(String(length=30), nullable=False, unique=True) # Can't be null and must be unique.
    email = Column(String(100), nullable=False, unique=True, comment="This one is the email.")
    date_created = Column(DateTime(), default=datetime.utcnow, nullable=True, unique=False, comment="The date when it was created.")

    def __repr__(self):
        return f"Users - {self.username}, {self.email}"


# This would shouw that there's a Users object in memory.
#print(user1)

# This gives you tha table name
#print(user1.__tablename__)

# You can also get the fields you  created.
#print(user1.username + " And " + user1.email)

# Gives you all the info about the table.
#print(user1.__table__)
