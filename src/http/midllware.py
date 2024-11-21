from io import BytesIO

from src.core.domain.errors import AbstractException
from src.core.util.logger.logger import Logger
from src.di.helper import http_helper


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

            Logger.error(f"{e.http_code} {e.message}", {"location": "ExceptionMiddleware"})

            return [f"{response}".encode('utf-8')]

class LogMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        self.log_request(environ)
        return self.app(environ, start_response)

    def get_request_body(self, environ):
        content_length = environ.get('CONTENT_LENGTH', '0')
        content_length = int(content_length) if content_length else 0

        if content_length > 0:
            body = environ['wsgi.input'].read(content_length)
            environ['wsgi.input'] = BytesIO(body)
            return body.decode('utf-8').replace('\n', '')
        return None

    def log_request(self, environ):
        method = environ.get('REQUEST_METHOD')
        url = environ.get('PATH_INFO')
        body = self.get_request_body(environ)

        http_helper.log_request(body,f"{method} {url}")


