import uuid
from src.core.util.helper.validator import Validator


class BaseEntity:

    __uuid: str
    _validator: Validator

    @property
    def id(self):
        return self.__uuid

    @id.setter
    def id(self, value):
        self._validator.validate_type(value, str).validate()
        self.__uuid = value

    def get_uuid(self):
        return str(uuid.uuid4())

    def inner_eq(self, other):
        if not isinstance(other, BaseEntity):
            return False

        return self.id == other.id

    def __eq__(self, other):
        return self.inner_eq(other)

    @property
    def validator(self):
        return self._validator

    def __init__(self):
        self.__uuid = self.get_uuid()
        self._validator = Validator()

