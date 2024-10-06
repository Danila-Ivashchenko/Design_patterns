from abstract import typed_none

from entity.base import BaseEntity
from entity.measurement_unit import MeasurementUnit


class Nomenclature(BaseEntity):

    __name: str
    __nomenclature_group_id: str
    __measurement_unit: MeasurementUnit

    def __init__(self, name: str = "", nomenclature_group_id: str = "", measurement_unit: MeasurementUnit = None):
        super().__init__()

        self._validator.validate_type(name, str).validate_max_or_equal_length(name, 255)
        self._validator.validate_type(nomenclature_group_id, str)
        self._validator.validate_type_or_none(measurement_unit, MeasurementUnit)

        self._validator.validate()

        self.__name = name
        self.__nomenclature_group_id = nomenclature_group_id

        self.__measurement_unit = measurement_unit



    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self._validator.validate_type(value, str).validate_max_or_equal_length(value, 255).validate()

        self.__name = value

    @property
    def nomenclature_group_id(self):
        return self.__nomenclature_group_id

    @nomenclature_group_id.setter
    def nomenclature_group_id(self, value: str):
        self._validator.validate_type(value, str).validate()

        self.__nomenclature_group_id = value

    @property
    @typed_none(MeasurementUnit)
    def measurement_uint(self):
        return self.__measurement_unit

    @measurement_uint.setter
    def measurement_uint(self, value: MeasurementUnit):
        self._validator.validate_type(value, MeasurementUnit).validate()

        self.__measurement_unit = value

    def __repr__(self):
        return f"{self.__name} {self.__nomenclature_group_id} {self.__measurement_unit}"



