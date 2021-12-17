import logging
# from icecream import ic
from flask import current_app, Blueprint  # request, Flask,

blueprint = Blueprint('api', __name__)
environment = current_app.ms_actions.config['environment']


@blueprint.route('/')
def index():
    logging.debug('Esto es un mensaje de debug')
    return {"msg": "This is an example app"}

# @api.route('/<name>')
# class IndexClass(Resource):
#     def get(self, name):
#         logging.debug('Esto es un mensaje de debug')
#         resp = current_app.ms_actions.do_something(name)
#         return {'msg': resp}
