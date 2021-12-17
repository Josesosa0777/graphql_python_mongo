"""Micro service core actions."""

import logging
from icecream import ic
from ariadne import convert_kwargs_to_snake_case
from ariadne import load_schema_from_path, make_executable_schema, snake_case_fallback_resolvers, ObjectType

# En este paquete va la clase que representa las acciones que implementara el
# microservicio.


class Actions:
    """Clase de acciones del Core.

    En esta clase se definen y se implementan todas las acciones que
    realizara el microservicio.
    """

    def __init__(self, config=None, db=None):
        """Object constructor."""
        logging.info("Init actions")
        self.config = config
        self.db = db
        self.query = ObjectType("Query")
        self.mutation = ObjectType("Mutation")
        self.query.set_field("users", self.resolve_users)
        self.query.set_field("user", self.resolve_user)
        self.mutation.set_field("createUser", self.resolve_create_user)
        self.mutation.set_field("checkUserPasswd", self.resolve_check_user_passwd)
        self.type_defs = load_schema_from_path("microservice/core/actions/schema.graphql")
        self.schema = make_executable_schema(
            self.type_defs,
            self.query,
            self.mutation,
            snake_case_fallback_resolvers
        )

    @convert_kwargs_to_snake_case
    def resolve_users(self, obj, info):
        # pylint: disable=W0612,W0613
        return self.db.list_users()

    @convert_kwargs_to_snake_case
    def resolve_user(self, obj, info, user_id):
        # pylint: disable=W0612,W0613
        return self.db.get_user(user_id)

    @convert_kwargs_to_snake_case
    def resolve_create_user(self, obj, info, email, passwd):
        # pylint: disable=W0612,W0613
        return self.db.new_user(email, passwd)

    @convert_kwargs_to_snake_case
    def resolve_check_user_passwd(self, obj, info, email, passwd):
        # pylint: disable=W0612,W0613
        return self.db.check_user_passwd(email, passwd)
