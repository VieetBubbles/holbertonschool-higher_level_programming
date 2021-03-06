#!/usr/bin/python3
# Write a script that prints the State object with the name passed as argument
# from the database hbtn_0e_6_usa

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format("root", "root", sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # HERE: no SQL query, only objects!

    states = session.query(State)
    table = states.filter_by(name=state_name).first()
    if table:
        print(table.id)
    else:
        print("Not found")

    session.close()
