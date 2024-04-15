#!/usr/bin/python3
""" deletes all State objects with a name containing
    the letter a from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                               format(argv[1],
                                      argv[2],
                                      argv[3]),
                               pool_pre_ping=True)

        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()

        for instance in session.query(State).filter(State.name.like('%a%')):
            session.delete(instance)
        session.commit()
        session.close()
        engine.dispose()
    except SQLAlchemyError as e:
        print(e)
