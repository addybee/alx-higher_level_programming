#!/usr/bin/python3
""" adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
        louisiana_state = State(name="Louisiana")
        session.add(louisiana_state)
        session.commit()
        query = session.query(State).filter_by(name="Louisiana").scalar()

        if query:
            print(query.id, query.name)
        session.close()
        engine.dispose()
    except SQLAlchemyError as e:
        print(e)
