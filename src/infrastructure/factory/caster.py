import datetime

from src.core.util.helper.validator import Validator


class TypeCaster:

    __type_to_func = {}

    __validator: Validator

    def __init__(self):
        self.__validator = Validator()

        self.__type_to_func = {
            datetime.datetime: self.__datetime
        }

    def cast(self, value, type_to_cast):
        if isinstance(value, type_to_cast):
            return value

        if isinstance(value, (list, tuple)):
            return [self.cast(v, type_to_cast) for v in value]

        return self.__cast(value, type_to_cast)

    def __cast(self, value, type_to_cast):
        if type_to_cast in self.__type_to_func.keys():
            return self.__type_to_func[type_to_cast](value)

        return type_to_cast(value)

    def __datetime(self, value):
        if isinstance(value, int):
            return datetime.datetime.fromtimestamp(value)
        if isinstance(value, str):
            return datetime.datetime.fromisoformat(value)

        return None