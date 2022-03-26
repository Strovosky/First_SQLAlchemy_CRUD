# In this module, we're going to create the engine

from sqlalchemy import create_engine

from main import Base

engine = create_engine("mysql+pymysql://root@localhost:3306/db_test")

# This one tells the engine to create all the info of the table.
Base.metadata.create_all(engine)

