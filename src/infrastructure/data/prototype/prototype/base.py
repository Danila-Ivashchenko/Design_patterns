from abc import ABC, abstractmethod
from src.infrastructure.data.prototype.filter.entry.filter_entry import FilterEntry
from src.infrastructure.data.prototype.filter.filter.base import Filter
from src.infrastructure.data.prototype.filterer.base import BaseFilterer
from src.infrastructure.factory.opeatation import OperationMapper
from src.core.util.helper.validator import Validator
from src.core.util.helper.common import CommonParser


class BasePrototype(ABC):

    __data: list
    _operation_mapper: OperationMapper
    _validator: Validator
    _common_parser: CommonParser
    _filterer: BaseFilterer

    def __init__(self, data):
        self.__data = data
        self._validator = Validator()
        self._operation_mapper = OperationMapper()
        self._common_parser = CommonParser()
        self._filterer = BaseFilterer()

    @property
    def data(self):
        return self.__data

    @abstractmethod
    def create(self, filter_dto: list[FilterEntry]) -> list:
        pass

    def _filter_by_field_name(self, entry: FilterEntry, data: list):
        if entry == None:
            return data

        operation = self._operation_mapper.enum_to_operation(entry.operation)

        result = self._filterer.filter(data, entry.key, entry.value, operation, entry.recursive)
        return result

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

    def __item(self, item, field_name: str, value: any, operation, structure: str = None) -> bool:
        item_fields = self._common_parser.parse_fields(item)

        ok = False

        for item_field in item_fields:
            if ok:
                break

            item_val = getattr(item, item_field)
            if item_field == field_name:
                ok = operation(item_val, value)
            else:
                if structure != None:
                    structure_items = structure.split('.')

                    if len(structure_items) > 0:
                        current_structure_item = structure_items[0]
                        if item_field == current_structure_item:
                            new_structure = None
                            if len(structure_items) > 1:
                                new_structure = '.'.join(structure_items[1:])

                            ok = self.__item(item_val, field_name, value, operation, new_structure)
        return ok

    def __list(self, data: list, field_name: str, value: any, operation):
        self._validator.validate_type(field_name, str).validate()

        res = []

        for item in data:
            if self.__item(item, field_name, value, operation):
                res.append(item)

        return res

    def __item_primitive(self, item, field_name: str, value: any, operation, structure: str = None):
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
                if field_name == structure:
                    ok = self.__item(item_val, field_name, value, operation)

        return ok

    def __item_list(self, items: list, field_name: str, value: any, operation, structure: str = None):
        self._validator.validate_type(field_name, str)
        if not isinstance(items, list):
            return False

        for item in items:
            if self.__item(item, field_name, value, operation, structure):
                return True
        return False