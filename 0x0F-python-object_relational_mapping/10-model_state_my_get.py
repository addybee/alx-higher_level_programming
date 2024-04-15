#!/usr/bin/python3
""" prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa
"""

from model_state import Base, State
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
        Session = sessionmaker(bind=engine)
        session = Session()
        query = session.query(State).\
            filter(State.name == argv[4]).\
            order_by(State.id)
        result = query.one_or_none()
        if result:
            print(result.id)
        else:
            print("Not found")
        session.close()
        engine.dispose()
    except SQLAlchemyError as e:
        print(e)
