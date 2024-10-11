from abc import ABC, abstractmethod
from prototype.filter import Filter
from prototype.filter.operations import OperationMapper
from helper import Validator


class BasePrototype(ABC):

    __data: list
    _operation_mapper: OperationMapper
    _validator: Validator

    def __init__(self, data):
        self.__data = data
        self._validator = Validator()
        self._operation_mapper = OperationMapper()

    @property
    def data(self):
        return self.__data

    @abstractmethod
    def create(self, filter_dto: Filter):
        pass
