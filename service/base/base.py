from helper import Validator
from errors.abstract import AbstractException


class BaseService:
    _validator: Validator
    __error: AbstractException = None

    def __init__(self):
        self._validator = Validator()

    @property
    def error(self):
        return self.__error