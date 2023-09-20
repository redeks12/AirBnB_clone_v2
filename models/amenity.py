#!/usr/bin/python3
""" State Module for HBNB project """
import os

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel
from models.place import Place, place_amenity

HBNB_STORAGE_TYPE = os.environ.get("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    if HBNB_STORAGE_TYPE == "db":
        place_amenities = relationship(
            "Place",
            secondary=place_amenity,
            back_populates="amenities",
            viewonly=False,
        )
