
class TypedList(list):
    __elem_type: type

    def __init__(self, elem_type: type, l: list = None):
        super().__init__()
        self.__elem_type = elem_type

        if isinstance(l, list):
            self.extend(l)

    @property
    def elem_type(self):
        return self.__elem_type

    @elem_type.setter
    def elem_type(self, t: type):
        self.__elem_type = t


def typed_list(t: type):
    def inner_decorator(f):
        def wrapper(self):
            original_list = f(self)
            if isinstance(original_list, TypedList):
                original_list.elem_type = t

            return TypedList(t, original_list)

        return wrapper

    return inner_decorator