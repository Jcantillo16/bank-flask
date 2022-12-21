import json
import traceback
from flask import Flask, make_response
from werkzeug.exceptions import HTTPException
from src.controllers import title_api
from src.config.app_config import config_by_name


def _handle_exception(error: Exception):
    """
      This method changes default HTML response format
      into JSON format for exceptions.
    """

    if isinstance(error, HTTPException):
        response = error.get_response()
        response.data = json.dumps({
            'code': error.code,
            'name': error.name,
            'description': error.description
        })

        response.content_type = 'application/json'
    else:
        traceback.print_exc()

        response = json.dumps({
            'code': 500,
            'name': 'internal server error',
            'description': 'Something is wrong here, try later'
        })
        response = make_response(response, 500)
        response.headers['Content-Type'] = 'application/json'
    
    return response


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.app_context().push()

    app.register_blueprint(title_api, url_prefix='/title')
    app.errorhandler(Exception)(_handle_exception)

    return app
