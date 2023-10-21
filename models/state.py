#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:

        @property
        def cities(self):
            """Return the cities"""
            from models import storage

            cit = []
            store = storage.all(City)
            for key, city in store.items():
                if self.id == city.state_id:
                    cit.append(city)
            return cit
