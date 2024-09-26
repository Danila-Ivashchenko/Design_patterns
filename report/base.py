from enums import ReportType
from abc import ABC, abstractmethod
from helper import CommonParser, Validator
from errors import ArgumentException


class BaseReporter(ABC):

    _parser: CommonParser
    _validator: Validator

    def __init__(self):
        self._parser = CommonParser()
        self._validator = Validator()

    @abstractmethod
    def report(self, data):
        pass

    def _to_serializable(self, val):
        if isinstance(val, dict):
            return {str(k): self._to_serializable(v) for k, v in val.items()}
        elif isinstance(val, list):
            return [self._to_serializable(v) for v in val]
        elif hasattr(val, '__dict__'):
            fields = self._parser.parse_fields(val)
            return {field: self._to_serializable(getattr(val, field)) for field in fields if not callable(getattr(val, field))}
        elif hasattr(val, '__str__'):
            return str(val)
        else:
            return val

    def _get_main_class_name(self, data):
        if isinstance(data, list) and len(data) > 0:
            return data[0].__class__.__name__

        return data.__class__.__name__