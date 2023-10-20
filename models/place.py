#!/usr/bin/python3
""" Place Module for HBNB project """
import os

from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)
HBNB_STORAGE_TYPE = os.environ.get("HBNB_TYPE_STORAGE")


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"
    amenity_ids = []
    if HBNB_STORAGE_TYPE == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            viewonly=False,
            back_populates="place_amenities",
        )
    else:

        @property
        def reviews(self):
            """Returns a list of reviews associated with this place"""
            from models import storage
            from models.review import Review

            review_with_ids = []
            revs = storage.all(Review)
            for key, rev in revs:
                if rev.place_id == self.id:
                    review_with_ids.append(rev)

            return review_with_ids

        @property
        def amenities(self):
            """return a list of amenities associated with this place"""
            from models import storage
            from models.amenity import Amenity

            amenities_with_ids = []
            ams = storage.all(Amenity)
            for key, amm in ams:
                if amm.place_id == self.id:
                    amenities_with_ids.append(amm)

            return amenities_with_ids

        @amenities.setter
        def amenities(self, amm):
            from models.amenity import Amenity

            if type(amm) == Amenity:
                self.amenity_ids.append(amm.id)
