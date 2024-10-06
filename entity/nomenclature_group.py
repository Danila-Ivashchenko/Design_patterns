from entity.base import BaseEntity


class NomenclatureGroup(BaseEntity):

    __name = ""

    def __init__(self, name: str = ""):
        super().__init__()

        self._validator.validate_type(name, str).validate()

        self.__name = name


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self._validator.validate_type(value, str).validate()

        self.__name = value

    def inner_eq(self, other):
        if not isinstance(other, NomenclatureGroup):
            return False

        return self.name == other.name