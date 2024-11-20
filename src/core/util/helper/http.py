from src.di.observer import observer
from .json import JsonHelper
from .validator import Validator
from ...domain.enums.event_type import EventType
from ...domain.errors import AbstractException

class RequestModel:
    route: str = ""
    request: dict = {}

    def __init__(self, route: str, request: dict):
        self.route = route
        if dict is not None:
            self.request = request

    def __str__(self):
        return f'route: "{self.route}", body: "{self.request}"'

class HttpHelper:

    __json_helper: JsonHelper
    __validator: Validator

    def __init__(self):
        self.__json_helper = JsonHelper()
        self.__validator = Validator()

    def __response(self, data: dict, code: int):
        return data, code

    def response(self, data, code: int):
        self.__validator.validate_type(code, int).validate()

        serialized_data = self.__json_helper.to_serialize(data)

        return self.__response(serialized_data, code)

    def response_ok(self, data):
        serialized_data = self.__json_helper.to_serialize(data)

        return self.__response(serialized_data, 200)

    def response_error(self, e: AbstractException) -> dict:
        result = {}

        error_value = "somthing went wrong..."

        if e.to_response:
            error_value = e.message

        result["error"] = error_value

        return result

    def log_request(self, data: dict, route: str):
        observer.notify(EventType.GOT_HTTP_REQUEST, RequestModel(route, data))

    def parse_request(self, t: type, data: dict):
        self.__validator.validate_type(t, type).validate()

        return self.__json_helper.to_deserialize(t, data)