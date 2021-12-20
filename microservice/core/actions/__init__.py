"""Micro service core actions."""

import logging
import json
from icecream import ic
from ariadne import convert_kwargs_to_snake_case
from ariadne import load_schema_from_path, make_executable_schema, snake_case_fallback_resolvers, ObjectType
from influxdb_client.client.flux_table import FluxStructureEncoder
# En este paquete va la clase que representa las acciones que implementara el
# microservicio.


class Actions:
    """Clase de acciones del Core.

    En esta clase se definen y se implementan todas las acciones que
    realizara el microservicio.
    """

    def __init__(self, config=None, db=None, db_stat=None):
        """Object constructor."""
        logging.info("Init actions")
        self.config = config
        self.db = db
        self.db_stat = db_stat
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
        res = self.db.new_user(email, passwd)
        # data = self.db_stat.get_measurement("TEST_NeighborBGPstate", "-30d")
        self.show_measurement_summary("TEST_NeighborBGPstate", "-8d")
        # output = json.dumps(data, cls=FluxStructureEncoder, indent=4)
        # print("---\n", output)
        # print("res: ", data.)
        return res
    @convert_kwargs_to_snake_case
    def resolve_check_user_passwd(self, obj, info, email, passwd):
        # pylint: disable=W0612,W0613
        return self.db.check_user_passwd(email, passwd)

    @convert_kwargs_to_snake_case
    def resolve_create_indicator(self, obj, info, email, passwd):
        # pylint: disable=W0612,W0613
        return self.db.new_user(email, passwd)

    def show_measurement_summary(self, measurement, since):
        """Get a specific kpi measurement."""
        data = self.db_stat.get_measurement(measurement, since)
        if not data:
            abort(404, "Not found")

        # import json
        # from influxdb_client.client.flux_table import FluxStructureEncoder
        output = json.dumps(data, cls=FluxStructureEncoder, indent=4)
        print(output)

        response = {"data": {}}
        for table in data:
            aux = []
            for row in table.records:
                structure = {}
                for key in row.values:
                    # Parse datetime formats to iso-format or string to avoid errors in json response
                    if key == '_start' or key == '_stop' or key == '_time':
                        structure[key] = row.values[key].isoformat()
                    else:
                        structure[key] = row.values[key]
                aux.append(structure)
            response['data'][f'table {table.records[0].table}'] = aux
        print("___ ", response)
        return response