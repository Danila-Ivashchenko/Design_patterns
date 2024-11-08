from src.core.domain.service.base.base import BaseService
from src.core.util.helper.validator import Validator
from src.core.util.observer.event import Event


class Observer:

    __observers = []
    __validator: Validator = Validator()

    def register(self, observer):
        self.__validator.validate_type(observer, BaseService)

        found = [o for o in Observer.__observers if o.__class__ == observer.__class__]

        if len(found) == 0:
            Observer.__observers.append(observer)

    def notify(self, event_type, payload):
        event = Event()
        event.type = event_type
        event.payload = payload

        for observer in Observer.__observers:
            observer.handle_event(event)