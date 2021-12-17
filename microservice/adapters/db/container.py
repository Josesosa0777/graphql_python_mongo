from dependency_injector import containers, providers
import pymongo
from microservice.adapters.db.implementation import DB


class DBase(containers.DeclarativeContainer):
    config = providers.Configuration()
    mclient = providers.Singleton(pymongo.MongoClient, config.connection_string)
    database = providers.Singleton(DB, session=mclient)
