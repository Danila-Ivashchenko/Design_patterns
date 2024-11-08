

class AbstractException(Exception):

    __message = ""
    __http_code = 500
    __to_response = False

    def __init__(self, message: str, code: int = 400, to_response: bool = False):
        self.__message = message
        self.__http_code = code
        self.__to_response = to_response

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def http_code(self):
        return self.__http_code

    @http_code.setter
    def http_code(self, http_code: int):
        self.__http_code = http_code


    @property
    def to_response(self) -> bool:
        return self.__to_response

    @to_response.setter
    def to_response(self, to_response: bool):
        self.__to_response = to_response



