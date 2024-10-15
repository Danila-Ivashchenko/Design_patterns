import datetime
from abc import ABC, abstractmethod

from src.core.domain.entity.base import BaseEntity
from src.core.util.helper.common import CommonParser
from src.core.util.helper.validator import Validator


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
        elif isinstance(val, (int, float, bool)):
            return val
        elif isinstance(val, datetime.datetime):
            return val.timestamp()
        elif hasattr(val, '__str__'):
            return str(val)
        else:
            return val

    def _get_main_class_name(self, data):
        if isinstance(data, list) and len(data) > 0:
            return data[0].__class__.__name__

        return data.__class__.__name__

    def _get_full_attrs_names(self, d: dict, parent_key: str = '', sep: str = '.') -> dict:
        items = {}
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(self._flatten_dict(v, new_key, sep=sep))
            else:
                items[new_key] = v
        return items

    def _get_list_properties(self, obj: list) -> list[dict]:
        res = []
        for item in obj:
            if hasattr(item, '__dict__'):
                res += [self._get_properties(item)]
            else:
                res += [item]
        return res

    def _get_properties(self, obj) -> dict:
        props = self._extract_properties(obj)

        if isinstance(obj, BaseEntity):
            props['id'] = obj.id

        props = self._process_nested_properties(props)

        return props

    def _extract_properties(self, obj) -> dict:
        return {
            key: getattr(obj, key)
            for key, value in obj.__class__.__dict__.items()
            if isinstance(value, property)
        }

    def _process_nested_properties(self, props: dict) -> dict:
        for key, value in props.items():
            if isinstance(value, list):
                props[key] = self._get_list_properties(value)
            elif hasattr(value, '__dict__') and not isinstance(value, (list, dict)):
                props[key] = self._get_properties(value)
            else:
                props[key] = value
        return props