import logging.config
from dependency_injector import containers, providers
from microservice.core.interfaces.db import DBAdapter, DBAdapterTimesSeries
from microservice.core.actions import Actions
from microservice.adapters.web import create_app


class Core(containers.DeclarativeContainer):
    config = providers.Configuration()
    log = providers.Resource(logging.config.dictConfig, config=config.logging)
    db = providers.Dependency(instance_of=DBAdapter)
    db_stat = providers.Dependency(instance_of=DBAdapterTimesSeries)
    actions = providers.Factory(Actions, config=config, db=db, db_stat=db_stat)
    web_app = providers.Factory(create_app, config=config.web, actions=actions)
