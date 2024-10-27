from os.path import split

from src.core.domain.enums.operation_type import OperationEnum
from src.core.util.helper.validator import Validator


class FilterEntry:
    _key: str
    _value: any
    _operation: OperationEnum
    _recursive: bool

    __validator: Validator

    def __init__(self, key: str = "id", value: any = None, operation: OperationEnum | int = OperationEnum.Equal, recursive: bool = False):
        self.__validator = Validator()

        self.__validator.validate_type(key, str).validate_type(operation, OperationEnum)
        self.__validator.validate_on_of_type(operation, (OperationEnum, int)).validate()

        self._value = value
        self._key = key
        self._recursive = recursive

        if isinstance(operation, str):
            operation = OperationEnum(operation)

        self._operation = operation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v

    @property
    def operation(self) -> OperationEnum:
        return self._operation

    @operation.setter
    def operation(self, v: int | OperationEnum):
        self.__validator.validate_on_of_type(v, (int, OperationEnum))

        if not isinstance(v, OperationEnum):
            v = OperationEnum(v)
        self._operation = v

    @property
    def key(self) -> str:
        return self._key

    @key.setter
    def key(self, v: str):
        self.__validator.validate_type(v, str).validate()

        self._key = v

    @property
    def recursive(self) -> bool:
        return self._recursive

    @recursive.setter
    def recursive(self, v: bool):
        self.__validator.validate_type(v, bool).validate()

        self._recursive = v
