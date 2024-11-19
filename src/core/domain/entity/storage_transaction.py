from src.core.domain.abstract.typed_none import typed_none
from src.core.domain.entity.base import BaseEntity
from src.core.domain.entity.storage import Storage
from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.measurement_unit import MeasurementUnit
from src.core.domain.enums.storage_transaction_type import StorageTransactionType
from datetime import datetime


class StorageTransaction(BaseEntity):
    __storage: Storage = None
    __nomenclature: Nomenclature = None
    __count: float
    __type: StorageTransactionType = None
    __measurement_unit: MeasurementUnit = None
    __date_time: datetime


    @property
    @typed_none(Storage)
    def storage(self) -> Storage:
        return self.__storage

    @storage.setter
    def storage(self, value: Storage):
        self._validator.validate_type(value, Storage).validate()
        self.__storage = value

    @property
    @typed_none(Nomenclature)
    def nomenclature(self) -> Nomenclature:
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, value: Nomenclature):
        self._validator.validate_type(value, Nomenclature).validate()
        self.__nomenclature = value

    @property
    def count(self) -> float:
        return self.__count

    @count.setter
    def count(self, value: float | int):
        self._validator.validate_on_of_type(value, (float, int)).validate()

        self.__count = float(value)

    @property
    def type(self) -> StorageTransactionType:
        return self.__type

    @type.setter
    def type(self, value: StorageTransactionType | int):
        if isinstance(value, int):
            value = StorageTransactionType(value)

        self._validator.validate_type(value, StorageTransactionType).validate()
        self.__type = value

    @property
    @typed_none(MeasurementUnit)
    def measurement_unit(self) -> MeasurementUnit:
        return self.__measurement_unit

    @measurement_unit.setter
    def measurement_unit(self, value: MeasurementUnit):
        self._validator.validate_type(value, MeasurementUnit).validate()
        # primal_unit = value.primal_unit()
        self.__measurement_unit = value

    @property
    def date_time(self) -> datetime:
        return self.__date_time

    @date_time.setter
    def date_time(self, value: datetime | int | float):
        if isinstance(value, (int, float)):
            value = datetime.fromtimestamp(value)

        self._validator.validate_type(value, datetime).validate()
        self.__date_time = value

    @property
    def amount(self) -> float:
        delta_val = 0
        if self.type == StorageTransactionType.Consumption:
            delta_val = -1
        if self.type == StorageTransactionType.Arrival:
            delta_val = 1

        primal_unit = self.measurement_unit.primal_unit()

        return float(self.count * delta_val * primal_unit.ratio)

    @amount.setter
    def amount(self, value):
        pass


