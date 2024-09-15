import uuid
from abc import abstractmethod
from helper.validator import Validator


class BaseEntity:

    __uuid: str

    @property
    def id(self):
        return self.__uuid

    @id.setter
    def id(self, value):
        return

    @abstractmethod
    def get_uuid(self):
        pass

    def inner_eq(self, other):
        if not isinstance(other, BaseEntity):
            return False

        return self.id == other.id

    def __eq__(self, other):
        return self.inner_eq(other)

    def __init__(self):
        self.__uuid = self.get_uuid()

