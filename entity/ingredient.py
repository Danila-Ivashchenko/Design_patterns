from entity.base import BaseEntity
from entity.measurement_value import MeasurementValue
from entity.nomenclature import Nomenclature
from helper import Validator


class Ingredient(BaseEntity):

    __nomenclature: Nomenclature
    __measurement_value: MeasurementValue

    def __init__(self, nomenclature: Nomenclature, measurement_value: MeasurementValue):
        super().__init__()
        self._validator.validate_type(nomenclature, Nomenclature).validate_type(measurement_value, MeasurementValue).validate()
        self.__nomenclature = nomenclature
        self.__measurement_value = measurement_value

    @property
    def nomenclature(self):
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, nomenclatura):
        self._validator.validate_type(nomenclatura, Nomenclature).validate()
        self.__nomenclature = nomenclatura

    @property
    def measurement_value(self):
        return self.__measurement_value

    @measurement_value.setter
    def measurement_value(self, measurement_value):
        self._validator.validate_type(measurement_value, MeasurementValue).validate()
        self.__measurement_value = measurement_value


    def __repr__(self):
        return f"{self.__nomenclature} {self.__measurement_value}"