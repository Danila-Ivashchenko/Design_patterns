from datetime import datetime

from src.core.domain.entity.base import BaseEntity
from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.storage import Storage


class Osv(BaseEntity):
    __start_date: datetime
    __end_date: datetime
    __storage: Storage
    __nomenclature: Nomenclature
    __amount_at_start: float
    __amount_at_end: float

    @property
    def start_date(self) -> datetime:
        return self.__start_date

    @property
    def end_date(self) -> datetime:
        return self.__end_date

    @property
    def storage(self) -> Storage:
        return self.__storage

    @property
    def nomenclature(self) -> Nomenclature:
        return self.__nomenclature

    @property
    def amount_at_start(self) -> float:
        return self.__amount_at_start

    @property
    def amount_at_end(self) -> float:
        return self.__amount_at_end

    @start_date.setter
    def start_date(self, value: datetime | int | float):
        if isinstance(value, (int, float)):
            value = datetime.fromtimestamp(value)

        self._validator.validate_type(value, datetime).validate()
        self.__start_date = value

    @end_date.setter
    def end_date(self, value: datetime | int | float):
        if isinstance(value, (int, float)):
            value = datetime.fromtimestamp(value)

        self._validator.validate_type(value, datetime).validate()
        self.__end_date = value

    @amount_at_start.setter
    def amount_at_start(self, value: float | int):
        if isinstance(value, int):
            value = float(value)
        self._validator.validate_type(value, float).validate()
        self.__amount_at_start = value

    @amount_at_end.setter
    def amount_at_end(self, value: float | int):
        if isinstance(value, int):
            value = float(value)
        self._validator.validate_type(value, float).validate()
        self.__amount_at_end = value

    @storage.setter
    def storage(self, value: Storage):
        self._validator.validate_type(value, Storage).validate()
        self.__storage = value

    @nomenclature.setter
    def nomenclature(self, value: Nomenclature):
        self._validator.validate_type(value, Nomenclature).validate()
        self.__nomenclature = value



