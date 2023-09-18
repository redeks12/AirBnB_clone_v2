#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states", cascade="all, delete")

    @property
    def cities(self):
        from models.city import City
        from models import storage

        cit = []
        store = storage.all(City)
        for key, city in store:
            if self.id == city.state_id:
                cit.append(city)
        return cit
