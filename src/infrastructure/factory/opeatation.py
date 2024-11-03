from src.core.domain.enums.operation_type import OperationEnum
from src.core.domain.errors import OperationException


def equal(a, b):
    return a == b


def like(a, b):
    return b in a


def more(a, b):
    return a > b


def less(a, b):
    return a < b


def less_or_equal(a, b):
    return a <= b


def between(a, b):
    if isinstance(b, (list, tuple)):
        if len(b) == 2:
            return b[0] < a <= b[1]

    return False


class OperationMapper:
    __enum_to_operation = {
        OperationEnum.Equal: equal,
        OperationEnum.Like: like,
        OperationEnum.More: more,
        OperationEnum.Less: less,
        OperationEnum.Between: between,
        OperationEnum.LessOrEqual: less_or_equal
    }

    def enum_to_operation(self, operation: OperationEnum):
        if operation in self.__enum_to_operation.keys():
            return self.__enum_to_operation[operation]

        raise OperationException.operation_doesnt_set(operation)