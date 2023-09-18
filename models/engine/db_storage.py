#!/usr/bin/python3
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.amenity import Amenity
from models.base_model import Base, BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

HBNB_DB_NAME = os.environ.get("HBNB_MYSQL_DB")
HBNB_USER = os.environ.get("HBNB_MYSQL_USER")
HBNB_PWD = os.environ.get("HBNB_MYSQL_PWD")
HBNB_HOST = os.environ.get("HBNB_MYSQL_HOST")
HBNB_ENV = os.environ.get("HBNB_ENV")


class DBStorage:
    """mysql database storage"""

    __engine = None
    __session = None

    def __init__(self) -> None:
        """Initialize the database"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                HBNB_USER, HBNB_PWD, HBNB_HOST, HBNB_DB_NAME
            ),
            pool_pre_ping=True,
        )

    def all(self, cls=None):
        """gets all objects in the database"""
        objs = {}

        if cls is not None:
            queries = self.__session.query(cls).all()
            for query in queries:
                objs.update({"{}.{}".format(query.__class__.__name__, query.id): query})
            return objs
        else:
            classes = [User, BaseModel, City, State, Place, Review, Amenity]
            for class_ in classes:
                queries = self.__session.query(class_).all()
                for query in queries:
                    objs.update(
                        {"{}.{}".format(query.__class__.__name__, query.id): query}
                    )
            return objs

    def new(self, obj):
        """add a new object to the database"""
        self.__session.add(obj)

    def save(self):
        """save the object to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete the object from the database"""
        if obj is not None:
            queries = self.__session.query(obj).all()
            for query in queries:
                if query.id == obj.id:
                    self.__session.delete(query)

    def reload(self):
        """reload the session"""
        Base.metadata.create_all(self.__engine)
        some_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(some_session)
        self.__session = Session
