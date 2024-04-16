#!/usr/bin/python3
"""
creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

from relationship_state import State
from relationship_city import Base, City
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

        query = session.query(State).\
            filter(State.id == City.state_id).\
            order_by(State.id, City.id)
            
        for obj in query.all():
            print("{}: {}".format(obj.id, obj.name))
            for city in obj.cities:
                print("    {}: {}".format(city.id, city.name))
       
        session.close()
        engine.dispose()
    except SQLAlchemyError as e:
        print(e)
