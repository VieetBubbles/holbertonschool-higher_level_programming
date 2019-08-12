#!/usr/bin/python3
# Write a Python file similar to model_state.py named model_city.py
# that contains the class definition of a City.

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format("root", "root", sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # HERE: no SQL query, only objects!
    table = session.query(City, State).filter(City.state_id == State.id)

    for city, state in table:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
