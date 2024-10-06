from .abstract import AbstractException

class ArgumentException(AbstractException):

    @classmethod
    def invalid_type(cls, given, must_be):
        return cls(f"invalid type, given: {given}, must be: {must_be}")

    @classmethod
    def invalid_on_of_type(cls, given, must_be_list):
        return cls(f"invalid type, given: {given}, must be on of: {','.join([str(t) for t in must_be_list])}")

    @classmethod
    def invalid_min_length(cls, given, must_be):
        return cls(f"invalid length, given: {given}, must be bigger: {must_be}")

    @classmethod
    def invalid_max_length(cls, given, must_be):
        return cls(f"invalid length, given: {given}, must be lower: {must_be}")

    @classmethod
    def invalid_max_or_equal_length(cls, given, must_be):
        return cls(f"invalid length, given: {given}, must be lower or equal: {must_be}")

    @classmethod
    def invalid_less_value(cls, given, must_be_bigger):
        return cls(f"invalid value: given: {given}, must be bigger then: {must_be_bigger}")

    @classmethod
    def invalid_length(cls, given, must_be_bigger):
        return cls(f"invalid length of value: given: {given}, must be: {must_be_bigger}")

    @classmethod
    def invalid_value_exists(cls, given, list_of_values):
        return cls(f"invalid value: given: {given}, must be on of: {','.join([str(t) for t in list_of_values])}")