#!/usr/bin/python3
"""
creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

from relationship_state import Base, State
from relationship_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                               format(argv[1],
                                      argv[2],
                                      argv[3]),
                               pool_pre_ping=True)

        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()

        cali_state = State(name="vCalifornia",
                           cities=[City(name="San Francisco")])
        session.add(cali_state)
        session.commit()
        session.close()
        engine.dispose()
    except SQLAlchemyError as e:
        print(e)
