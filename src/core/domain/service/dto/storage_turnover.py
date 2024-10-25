from datetime import datetime

from src.core.domain.abstract.typed_list import typed_list
from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.storage import Storage
from src.infrastructure.data.prototype.filter.entry.filter_entry import FilterEntry


class StorageTurnoverDTO:
    __filters: list[FilterEntry] = None
    __start_time: datetime
    __end_time: datetime

    @property
    @typed_list(FilterEntry)
    def filters(self) -> list[FilterEntry]:
        return self.__filters

    @filters.setter
    def filters(self, value: list[FilterEntry]):
        self.__filters = value

    @property
    def start_time(self) -> datetime:
        return self.__start_time

    @start_time.setter
    def start_time(self, value: datetime):
        if isinstance(value, int):
            value = datetime.fromtimestamp(value)

        self.__start_time = value

    @property
    def end_time(self) -> datetime:
        return self.__end_time

    @end_time.setter
    def end_time(self, value: datetime | int):
        if isinstance(value, int):
            value = datetime.fromtimestamp(value)

        self.__end_time = value
