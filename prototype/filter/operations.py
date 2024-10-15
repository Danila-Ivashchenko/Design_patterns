from enum import Enum
from errors import OperationException


class OperationEnum(Enum):
    Equal = 1
    Like = 2
    More = 3
    Less = 4


def equal(a, b):
    return a == b


def like(a, b):
    return b in a


def more(a, b):
    return a > b


def less(a, b):
    return a < b


class OperationMapper:
    __enum_to_operation = {
        OperationEnum.Equal: equal,
        OperationEnum.Like: like,
        OperationEnum.More: more,
        OperationEnum.Less: less
    }

    def enum_to_operation(self, operation: OperationEnum):
        if operation in self.__enum_to_operation.keys():
            return self.__enum_to_operation[operation]

        raise OperationException.operation_doesnt_set(operation)