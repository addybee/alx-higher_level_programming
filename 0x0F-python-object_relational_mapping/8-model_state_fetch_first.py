#!/usr/bin/python3


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
        first_state = session.query(State).order_by(State.id).first()
        print("{}: {}".format(first_state.id, first_state.name))
        session.close()
        engine.dispose()
    except SQLAlchemyError as e:
        print(e)
