from datetime import datetime

from src.core.domain.abstract.typed_list import typed_list
from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.storage import Storage
from src.core.domain.service.dto.base_dto import BaseDTO
from src.infrastructure.data.prototype.filter.entry.filter_entry import FilterEntry


class StorageTurnoverDTO(BaseDTO):
    __filters: list[FilterEntry] = None
    __start_time: datetime = None
    __end_time: datetime = None

    @property
    @typed_list(FilterEntry)
    def filters(self) -> list[FilterEntry]:
        return self.__filters

    @filters.setter
    def filters(self, value: list[FilterEntry]):
        self._validator.validate_list_type(value, FilterEntry).validate()
        self.__filters = value

    @property
    def start_time(self) -> datetime:
        return self.__start_time

    @start_time.setter
    def start_time(self, value: datetime):
        self._validator.validate_on_of_type(value, (datetime, int)).validate()
        if isinstance(value, int):
            value = datetime.fromtimestamp(value)

        self.__start_time = value

    @property
    def end_time(self) -> datetime:
        return self.__end_time

    @end_time.setter
    def end_time(self, value: datetime | int):
        self._validator.validate_on_of_type(value, (datetime, int)).validate()
        if isinstance(value, int):
            value = datetime.fromtimestamp(value)

        self.__end_time = value
