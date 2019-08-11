#!/usr/bin/python3
# Write a script that adds the State object “Louisiana” to the
# database hbtn_0e_6_usa

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

    new_state = State(name='Louisiana')
    session.add(new_state)

    lou_ID = session.query(State).filter_by(name='Louisiana').first().id

    print(lou_ID)
    session.commit()
    session.close()
