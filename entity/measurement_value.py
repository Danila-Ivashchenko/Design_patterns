from entity.base import BaseEntity
from entity.measurement_unit import MeasurementUnit


class MeasurementValue(BaseEntity):

    __unit: MeasurementUnit
    __value: float

    def __init__(self, value: float = 0.0, unit: MeasurementUnit = None):
        super().__init__()
        self._validator.validate_type_or_none(value, float).validate_type_or_none(unit, MeasurementUnit).validate()
        self.__value = value

        if unit is None:
            unit = MeasurementUnit()

        self.__unit = unit

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self._validator.validate_type(value, float).validate()
        self.__value = value

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit):
        self._validator.validate_type(unit, MeasurementUnit).validate()
        self.__unit = unit

    def __repr__(self):
        return f"{self.__value} {self.__unit}"