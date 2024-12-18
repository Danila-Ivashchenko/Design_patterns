from src.infrastructure.data.prototype.filter.entry.filter_entry import FilterEntry
from src.infrastructure.data.prototype.prototype.base import BasePrototype


class StorageTransactionPrototype(BasePrototype):

    def create(self, filter_dto: list[FilterEntry]) -> list:
        data = self.data

        for entry in filter_dto:
            data = self._filter_by_field_name(entry, data)

        return data