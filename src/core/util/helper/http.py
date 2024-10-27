from .json import JsonHelper
from .validator import Validator


class HttpHelper:

    __json_helper: JsonHelper
    __validator: Validator

    def __init__(self):
        self.__json_helper = JsonHelper()
        self.__validator = Validator()

    def __response(self, data: dict, code: int):
        self.__validator.validate_type(code, int).validate()

        return data, code

    def response(self, data, code: int):
        self.__validator.validate_type(code, int).validate()

        serialized_data = self.__json_helper.to_serialize(data)

        return self.__response(serialized_data, code)

    def response_ok(self, data):
        serialized_data = self.__json_helper.to_serialize(data)

        return self.__response(serialized_data, 200)

    def parse_request(self, t: type, data: dict):
        self.__validator.validate_type(t, type).validate()

        return self.__json_helper.to_deserialize(t, data)