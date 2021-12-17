import logging
import bcrypt
import pymongo
import json
from bson import ObjectId, json_util
from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session
from pymongo.errors import InvalidURI, ConnectionFailure
from microservice.core.interfaces.db import DBAdapter
from microservice.core.exceptions import NoConfigFile

from microservice.core.model import User


class DB(DBAdapter):

    db = None

    # def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
    #     logging.info("Init db implementation")
    #     self.session_factory = session_factory
    #     logging.info('db object created')
    def __init__(self, connection_string=None):
        """Init."""
        if self.db is None:
            self.connect(connection_string)
        logging.info("db object created")
    
    def connect(self, connection_string=None):
        """Por favor agregar la docu de la funcion."""
        if connection_string is None:
            logging.critical("No config defined")
            raise NoConfigFile()
        try:
            self.db = pymongo.MongoClient(connection_string).get_default_database()
        except InvalidURI as e:
            print(e)
            logging.error("Invalid connection string.")
            raise
        except ConnectionFailure as e:
            print(e)
            logging.error("Connection failure.")
            raise

    def list_users(self):
        try:
            users_list = self.db.users.find()
            users = [user.to_dict() for user in users_list]
            payload = {
                "success": True,
                "users": users
            }
        except Exception as error:
            payload = {
                "success": False,
                "errors": [str(error)]
            }
        return payload

    def get_user(self, user_id):
        try:
            user = self.db.users.find_one({"_id": user_id})
            payload = {
                "success": True,
                "user": user
            }
        except Exception as error:
            payload = {
                "success": False,
                "errors": [str(error)]
            }
        return payload

    def new_user(self, email, password):
        try:
            hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
            print("hashed ", hashed_password)
            user = User(email=email, hashed_password=hashed_password, is_active=True)
            usr = user.to_dict()
            self.db.users.insert(user.to_dict())
            payload = {
                "success": True,
                "user": user
            }
        except Exception as error:
            print("EEEE")
            payload = {
                "success": False,
                "errors": [str(error)]
            }
        return payload

    # def check_user_passwd(self, email, password):
    #     with self.session_factory() as session:
    #         try:
    #             user = session.query(User).filter(User.email == email).first()
    #             if bcrypt.checkpw(password.encode("UTF-8"), user.hashed_password):
    #                 payload = {
    #                     "success": True,
    #                     "same": True
    #                 }
    #             else:
    #                 payload = {
    #                     "success": True,
    #                     "same": False
    #                 }
    #         except Exception as error:
    #             payload = {
    #                 "success": False,
    #                 "error": error
    #             }
    #         return payload

    def delete_user(self, user_id):
        pass

    def dummy(self):
        pass
