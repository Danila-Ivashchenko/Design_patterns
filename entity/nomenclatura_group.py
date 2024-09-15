from entity.base import BaseEntity
from helper.validator import Validator


class NomenclaturaGroup(BaseEntity):

    __name = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validator().validate_type(value, str).validate()

        self.__name = value

    def inner_eq(self, other):
        if not isinstance(other, NomenclaturaGroup):
            return False

        return self.title == other.title