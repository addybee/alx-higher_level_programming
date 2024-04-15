#!/usr/bin/python3
""" prints all City objects from the database hbtn_0e_14_usa
"""

from model_state import Base, State
from model_city import City
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

        query = session.query(State.name, City.id, City.name).\
            join(City).order_by(City.id)
        for row in query.all():
            print("{}: ({}) {}".format(*row))
        session.close()
        engine.dispose()
    except SQLAlchemyError as e:
        print(e)
