import datetime

from src.core.util.helper.common import CommonParser
from src.core.util.helper.validator import Validator
from enum import Enum

from src.infrastructure.factory.caster import TypeCaster


class BaseFilterer:

    _validator: Validator
    _common_parser: CommonParser
    __primitives = (str, int, float, bool)
    __type_to_filter: {}
    __caster = TypeCaster()

    def __init__(self):
        self._common_parser = CommonParser()
        self._validator = Validator()
        self.__type_to_filter = {
            list: self.__filter_list,
            Enum: self.__enum,
            datetime.datetime: self.__datetime,
        }

    def filter(self, data, field_name: str, value: any, operation, recursive: bool = False):
        return self.__list(data, field_name, value, operation, recursive)

    def __list(self, data: list, field_name: str, value: any, operation, recursive: bool = False) -> list:
        result = []

        for item in data:
            if self.__item(item, field_name, value, operation, recursive):
                result.append(item)

        return result

    def __item(self, item, field_name: str, value: any, operation, recursive: bool = False) -> bool:

        def_to_filter = self.__filter_item

        for key in self.__type_to_filter.keys():
            if isinstance(item, key):
                def_to_filter = self.__type_to_filter[key]

        return def_to_filter(item, field_name, value, operation, recursive)

    def __enum(self, item: Enum, field_name: str, value: any, operation, recursive: bool = False) -> bool:
        self._validator.validate_type(field_name, str)
        self._validator.validate_type(item, Enum)

        self._validator.validate()

        return operation(item.value, value)

    def __datetime(self, item: Enum, field_name: str, value: any, operation, recursive: bool = False) -> bool:
        self._validator.validate_type(field_name, str)
        self._validator.validate_type(item, datetime.datetime)
        self._validator.validate_on_of_type(value, (list, tuple))

        self._validator.validate()

        new_val = []

        for v in value:
            new_val.append(datetime.datetime.fromtimestamp(v))

        value = new_val

        return operation(item.value, value)

    def __filter_item(self, item, field_name: str, value: any, operation, recursive: bool = False) -> bool:
        self._validator.validate_type(field_name, str)
        self._validator.validate_type(field_name, str)

        self._validator.validate()

        item_fields = self._common_parser.parse_fields(item)

        ok = False

        field_names = field_name.split('.')

        if len(field_names) == 0:
            return False

        current_field_name = field_names[0]

        for item_field in item_fields:
            if ok:
                break

            item_val = getattr(item, item_field)

            if item_field == current_field_name:
                if len(field_names) > 1:
                    new_field_name = '.'.join(field_names[1:])
                    ok = self.__item(item_val, new_field_name, value, operation, recursive)
                else:
                    ok = self.__process_operation(item_val, value, operation)
            if isinstance(item, type(item_val)) and recursive:
                ok = self.__item(item_val, field_name, value, operation, recursive)

        return ok

    def __filter_list(self, items, field_name: str, value: any, operation, recursive: bool = False) -> bool:
        self._validator.validate_type(items, list)
        self._validator.validate_type(field_name, str)
        self._validator.validate()

        ok = False

        for list_item in items:
            if ok:
                break
            ok = self.__item(list_item, field_name, value, operation, recursive)

        return ok

    def __process_operation(self, value, key_value, operation):
        casted_key_value = self.__caster.cast(key_value, value.__class__)

        return operation(value, casted_key_value)


