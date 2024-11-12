from src.core.domain.enums.event_type import EventType
from src.core.util.helper.validator import Validator


class Event:
    __type: EventType
    __payload = None
    _validator: Validator

    def __init__(self):
        self._validator = Validator()

    @property
    def type(self):
        return self.__type

    @property
    def payload(self):
        return self.__payload

    @payload.setter
    def payload(self, payload):

        self.__payload = payload

    @type.setter
    def type(self, value: EventType):
        self._validator.validate_type(value, EventType).validate()

        self.__type = value