from errors import ArgumentException


class Validator:

    def __init__(self):
        self.__to_validate = []

    def validate_type(self, value, type_to_validate):
        self.__to_validate.append(lambda: self.__validate_type(value, type_to_validate))
        return self

    def validate_on_of_type(self, value, type_to_validate):
        self.__to_validate.append(lambda: self.__validate_on_of_type(value, type_to_validate))
        return self

    def validate_list_type(self, value, type_to_validate):
        self.__to_validate.append(lambda: self.__validate_type(value, list))
        self.__to_validate.append(lambda: self.__validate_list_type(value, type_to_validate))
        return self

    def validate_dict_types(self, value, type_to_validate_key, type_to_validate_value):
        self.__to_validate.append(lambda: self.__validate_type(value, dict))
        self.__to_validate.append(lambda: self.__validate_dict_types(value, type_to_validate_key, type_to_validate_value))
        return self

    def validate_type_or_none(self, value, type_to_validate):
        if value is None:
            return self

        self.__to_validate.append(lambda: self.__validate_type(value, type_to_validate))
        return self

    def validate_max_length(self, value, length: int):
        self.__to_validate.append(lambda: self.__validate_max_length(value, length))
        return self

    def validate_max_or_equal_length(self, value, length: int):
        self.__to_validate.append(lambda: self.__validate_max_or_equal_length(value, length))
        return self

    def validate_min_length(self, value, length: int):
        self.__to_validate.append(lambda: self.__validate_min_length(value, length))
        return self

    def validate_min_value(self, value, min_value):
        self.__to_validate.append(lambda: self.__validate_bigger(value, min_value))
        return self

    def validate_length(self, value, length: int):
        self.__to_validate.append(lambda: self.__validate_length(value, length))
        return self

    def validate_value_exists(self, value, list_of_values):
        self.__to_validate.append(lambda: self.__validate_value_exists(value, list_of_values))
        return self

    @staticmethod
    def __validate_max_length(value, length):
        if not len(value) < length:
            return ArgumentException.invalid_max_length(value, length)
        return None

    @staticmethod
    def __validate_max_or_equal_length(value, length):
        if len(value) > length:
            return ArgumentException.invalid_max_or_equal_length(len(value), length)
        return None

    @staticmethod
    def __validate_min_length(value, length):
        if not len(value) > length:
            return ArgumentException.invalid_min_length(value, length)
        return None

    @staticmethod
    def __validate_type(value, type_to_validate):
        if not isinstance(value, type_to_validate):
            return ArgumentException.invalid_type(type(value), type_to_validate)
        return None

    @staticmethod
    def __validate_on_of_type(value, types):
        for t in types:
            if isinstance(value, t):
                return None
        return ArgumentException.invalid_on_of_type(type(value), types)

    @staticmethod
    def __validate_list_type(value, type_to_validate):
        for v in value:
            if not isinstance(v, type_to_validate):
                return ArgumentException.invalid_type(type(v), type_to_validate)
        return None

    @staticmethod
    def __validate_dict_types(value, type_to_validate_key, type_to_validate_value):
        for k, v in value.items():
            if not isinstance(k, type_to_validate_key):
                return ArgumentException.invalid_type(type(k), type_to_validate_key)
            if not isinstance(v, type_to_validate_value):
                return ArgumentException.invalid_type(type(v), type_to_validate_value)
        return None

    @staticmethod
    def __validate_bigger(value, min_value):
        if value <= min_value:
            return ArgumentException.invalid_less_value(value, min_value)
        return None

    @staticmethod
    def __validate_length(value, must_be):
        if len(value) != must_be:
            return ArgumentException.invalid_length(value, must_be)
        return None

    @staticmethod
    def __validate_value_exists(value, list_of_values):
        if value not in list_of_values:
            return ArgumentException.invalid_value_exists(value, list_of_values)
        return None

    def validate(self):
        for f in self.__to_validate:
            ex = f()
            if ex is not None and isinstance(ex, Exception):
                raise ex

        self.__to_validate = []