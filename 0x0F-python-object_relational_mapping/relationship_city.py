#!/usr/bin/python3
"""
contains the class definition of a City
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """this class defines a city for ORM

    Args:
        Base (class): this is the declarative base class from model_state
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
