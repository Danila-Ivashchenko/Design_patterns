import uuid

from entity.base import BaseEntity
from entity.measurement_unit import MeasurementUnit



class Nomenclatura(BaseEntity):

    __name: str
    __nomenclatura_group_id: str
    __measurement_unit: MeasurementUnit

    def get_uuid(self):
        return str(uuid.uuid4())

    def __int__(self, name: str, nomenclature_group_id: str, measurement_unit: MeasurementUnit):
        self._validator.validate_type(name, str).validate_max_or_equal_length(name, 255)
        self._validator.validate_type(nomenclature_group_id, str)
        self._validator.validate_type(measurement_unit, MeasurementUnit)

        self._validator.validate()

        self.__name = name
        self.__nomenclatura_group_id = nomenclature_group_id
        self.__measurement_unit = measurement_unit

        super().__init__()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self._validator.validate_type(value, str).validate_max_or_equal_length(value, 255).validate()

        self.__name = value

    @property
    def nomenclatura_group_id(self):
        return self.__nomenclatura_group_id

    @nomenclatura_group_id.setter
    def nomenclatura_group_id(self, value: str):
        self._validator.validate_type(value, str).validate()

        self.__nomenclatura_group_id = value

    @property
    def measurement_uint(self):
        return self.__measurement_unit

    @measurement_uint.setter
    def measurement_uint(self, value: MeasurementUnit):
        self._validator.validate_type(value, MeasurementUnit).validate()

        self.__measurement_unit = value

    def __init__(self):
        super().__init__()



