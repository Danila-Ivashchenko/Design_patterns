from abc import ABC, abstractmethod
from .filter import Filter, FilterEntry
from .filter.operations import OperationMapper
from helper import Validator
from helper.common import CommonParser


class BasePrototype(ABC):

    __data: list
    _operation_mapper: OperationMapper
    _validator: Validator
    _common_parser: CommonParser

    def __init__(self, data):
        self.__data = data
        self._validator = Validator()
        self._operation_mapper = OperationMapper()
        self._common_parser = CommonParser()

    @property
    def data(self):
        return self.__data

    @abstractmethod
    def create(self, filter_dto: Filter):
        pass

    def _id(self, entry: FilterEntry, data: list):
        self._validator.validate_type_or_none(entry, FilterEntry).validate_type(data, list).validate()

        if entry == None:
            return data

        operation = self._operation_mapper.enum_to_operation(entry.operation)

        return self.__list(data, "id", entry.value, operation)

    def _name(self, entry: FilterEntry, data: list):
        self._validator.validate_type_or_none(entry, FilterEntry).validate_type(data, list).validate()

        if entry == None:
            return data

        operation = self._operation_mapper.enum_to_operation(entry.operation)

        return self.__list(data, "name", entry.value, operation)

    def __list(self, data: list, field_name: str, value: any, operation):
        self._validator.validate_type(field_name, str).validate()

        res = []

        for item in data:
            if self.__item(item, field_name, value, operation):
                res.append(item)

        return res

    def __item(self, item, field_name: str, value: any, operation):
        self._validator.validate_type(field_name, str)

        item_fields = self._common_parser.parse_fields(item)
        ok = False

        for item_field in item_fields:
            if ok:
                break

            item_val = getattr(item, item_field)
            if item_field == field_name:
                ok = operation(item_val, value)
            else:
                ok = self.__item(item_val, field_name, value, operation)

        return ok