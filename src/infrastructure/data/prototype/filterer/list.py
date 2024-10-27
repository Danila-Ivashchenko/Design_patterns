from src.infrastructure.data.prototype.filterer.base import BaseFilterer


class ListFilterer(BaseFilterer):

    def filter(self, item, field_name: str, value: any, operation, structure: str = None):
        self._validator.validate_type(item, list)
        self._validator.validate_type(field_name, str)
        self._validator.validate_type(value, any)
        self._validator.validate_type_or_none(structure, str)
        self._validator.validate()

