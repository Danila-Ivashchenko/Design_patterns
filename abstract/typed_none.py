class TypedNone:
    def __init__(self, elem_type: type):
        super().__init__()
        self.__elem_type = elem_type

    @property
    def elem_type(self):
        return self.__elem_type

    @elem_type.setter
    def elem_type(self, t: type):
        self.__elem_type = t

    def __eq__(self, other):
        if other is None or isinstance(other, TypedNone):
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


def typed_none(t: type = None):
    def inner_decorator(f):
        def wrapper(self):
            original_value = f(self)

            if original_value is not None:
                return original_value

            type_to_set = t

            if type_to_set is None:
                type_to_set = self.__class__

            if isinstance(original_value, TypedNone):
                original_value.elem_type = type_to_set
                return original_value

            return TypedNone(type_to_set)
        return wrapper
    return inner_decorator