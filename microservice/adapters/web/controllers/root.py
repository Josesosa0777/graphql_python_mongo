import logging
from icecream import ic
from flask import current_app, Blueprint, request, jsonify
from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML

blueprint = Blueprint('root', __name__)
environment = current_app.ms_actions.config['environment']


@blueprint.route('/')
def index():
    logging.debug('Esto es un mensaje de debug')
    return "TEST001"


@blueprint.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@blueprint.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        current_app.ms_actions.schema,
        data,
        context_value=request,
        debug=current_app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
