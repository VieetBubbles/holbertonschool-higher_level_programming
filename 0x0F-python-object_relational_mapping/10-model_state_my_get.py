#!/usr/bin/python3
# Write a script that prints the State object with the name passed as argument
# from the database hbtn_0e_6_usa

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format("root", "root", sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    # HERE: no SQL query, only objects!
    for state in session.query(State).order_by(State.id).all():
        if sys.argv[4] == state.name:
            var = state.id
            break
        else:
            var = "Not found"
    print("{}".format(var))
    session.close()
