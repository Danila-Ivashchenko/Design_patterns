from abc import abstractmethod

from src.core.domain.enums.event_type import EventType
from src.core.util.helper.validator import Validator
from src.core.domain.errors import AbstractException
from src.core.util.observer.event import Event


class BaseService:
    _validator: Validator
    __error: AbstractException = None

    def __init__(self):
        self._validator = Validator()

    @property
    def error(self):
        return self.__error

    def set_error(self, e: AbstractException):
        self._validator.validate_type(e, AbstractException).validate()

        self.__error = e

    @abstractmethod
    def handle_event(self, event: Event):
        self._validator.validate_type(event, Event).validate()