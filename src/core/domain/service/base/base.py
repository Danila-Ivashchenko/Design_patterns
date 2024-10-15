from src.core.util.helper.validator import Validator
from src.core.domain.errors import AbstractException


class BaseService:
    _validator: Validator
    __error: AbstractException = None

    def __init__(self):
        self._validator = Validator()

    @property
    def error(self):
        return self.__error

    def set_error(self, e: AbstractException):
        self._validator.validate_type(e, AbstractException).validate()

        self.__error = e