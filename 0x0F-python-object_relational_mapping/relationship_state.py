#!/usr/bin/python3
"""
contains the improve class definition of a State and an instance
Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, registry
from relationship_city import City, Base


class State(Base):
    """this class defines a state for ORM

    Args:
        Base (class): this is the declarative base class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="states")


City.state = relationship("State", back_populates="cities")
mapper_registry = registry()
mapper_registry.configure()