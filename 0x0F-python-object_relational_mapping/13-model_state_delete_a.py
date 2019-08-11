#!/usr/bin/python3
# Write a script that deletes all State objects with a name containing
# the letter a from the database hbtn_0e_6_usa

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format("root", "root", sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # HERE: no SQL query, only objects!

    states = session.query(State).filter(State.name.like('%a%')).all()
    for row in states:
        session.delete(row)

    session.commit()
    session.close()
