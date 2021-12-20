import logging
import sys
from os import getenv
import click
from icecream import ic
from dependency_injector import providers
from microservice.adapters.db.implementation import DB
from microservice.adapters.db_influx import DBTimeSeries
from microservice.core import Core


def core_init():
    config = getenv('MS_CONFIG')
    if config is None:
        ic()
        click.echo(
            click.style(
                'MS_CONFIG variable is not defined',
                fg='red',
                bold=True
            )
        )
        sys.exit(1)
    core_container = Core()
    core_container.config.from_yaml(config)
    core_container.db.override(
        providers.Singleton(DB, connection_string=core_container.config.db.connection_string)
    )
    core_container.db_stat.override(
        providers.Singleton(DBTimeSeries,
                            connection_string=core_container.config.db_time_series.connection_string,
                            token=core_container.config.db_time_series.token,
                            default_org=core_container.config.db_time_series.default_org,
                            default_bucket=core_container.config.db_time_series.default_bucket)

    )
    core_container.init_resources()
    logging.info('logging initialized')
    return core_container


@click.group()
def cli():
    """General command line interface."""


@cli.group(help='Webserver commands')
def web():
    pass


@cli.group(help='Miscellaneous commands')
def misc():
    pass


@cli.group(help='Database commands')
def db():
    pass


@web.command(help='Run web dev server')
def run():
    core_obj = core_init()
    web_app = core_obj.web_app()
    web_app.run()


if __name__ == '__main__':
    cli()
