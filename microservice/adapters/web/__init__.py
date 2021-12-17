import logging
from icecream import ic
from flask import Flask
from microservice.core.exceptions import NoConfigFile


def create_app(config=None, actions=None):
    if config is None:
        msg = 'Config file variable is not defined'
        logging.critical(msg)
        raise NoConfigFile(msg)
    logging.info('creating web app')
    app = Flask(__name__, instance_relative_config=True)
    for k, v in config.items():
        app.config[k] = v
    app.ms_actions = actions

    with app.app_context():
        from microservice.adapters.web.controllers.root import blueprint as root
        from microservice.adapters.web.controllers.test import blueprint as test
        app.register_blueprint(root)
        app.register_blueprint(test, url_prefix="/test")

    return app
