import logging.config
from dependency_injector import containers, providers
from microservice.core.interfaces.db import DBAdapter
from microservice.core.actions import Actions
from microservice.adapters.web import create_app


class Core(containers.DeclarativeContainer):
    config = providers.Configuration()
    log = providers.Resource(logging.config.dictConfig, config=config.logging)
    db = providers.Dependency(instance_of=DBAdapter)
    actions = providers.Factory(Actions, config=config, db=db)
    web_app = providers.Factory(create_app, config=config.web, actions=actions)
