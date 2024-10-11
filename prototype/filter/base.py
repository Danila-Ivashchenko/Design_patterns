from .operations import OperationEnum


class FilterEntry:
    _value: any
    _operation: OperationEnum

    def __init__(self, value: any = None, operation: OperationEnum | str = OperationEnum.Equal):
        self._value = value
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
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, v):
        if not isinstance(v, OperationEnum):
            v = OperationEnum(v)
        self._operation = v


class Filter:
    pass