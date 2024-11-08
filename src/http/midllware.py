
from src.core.domain.errors import AbstractException
from src.di.helper import http_helper
from functools import wraps


class ExceptionMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        try:
            return self.app(environ, start_response)
        except AbstractException as e:
            status = f"{e.http_code} {e.message}"
            headers = [('Content-Type', 'text/plain')]

            start_response(status, headers)

            response = http_helper.response_error(e)

            return [f"{response}".encode('utf-8')]
