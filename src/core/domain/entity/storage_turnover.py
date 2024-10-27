import datetime

from src.core.domain.entity.base import BaseEntity
from src.core.domain.entity.measurement_unit import MeasurementUnit
from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.storage import Storage


class StorageTurnover(BaseEntity):

    __storage: Storage = None
    __nomenclature: Nomenclature = None
    __measurement_unit: MeasurementUnit = None
    __amount: float

    @property
    def storage(self) -> Storage:
        return self.__storage

    @storage.setter
    def storage(self, value: Storage):
        self._validator.validate_type(value, Storage).validate()
        self.__storage = value

    @property
    def nomenclature(self) -> Nomenclature:
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, value: Nomenclature):
        self._validator.validate_type(value, Nomenclature).validate()
        self.__nomenclature = value

    @property
    def measurement_unit(self) -> MeasurementUnit:
        return self.__measurement_unit

    @measurement_unit.setter
    def measurement_unit(self, value: MeasurementUnit):
        self._validator.validate_type(value, MeasurementUnit).validate()
        self.__measurement_unit = value

    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, value: float):
        self._validator.validate_type(value, float).validate()
        self.__amount = value
