import uuid
from copy import deepcopy

from entity.base import BaseEntity
from helper.validator import Validator

class MeasurementUnit(BaseEntity):

    __name: str
    __ratio: float
    __parent_unit = None

    def __init__(self, name: str, ratio: float = 1.0, parent_unit = None):
        super().__init__()
        self._validator.validate_type(name, str)
        self._validator.validate_type(ratio, float).validate_min_value(ratio, 0)
        self._validator.validate_type_or_none(parent_unit, MeasurementUnit)

        self._validator.validate()

        self.__name = name
        self.__ratio = ratio
        self.__parent_unit = parent_unit



    def get_uuid(self):
        return str(uuid.uuid4())

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self._validator.validate_type(value, str).validate()

        self.__name = value

    @property
    def ratio(self):
        return self.__ratio

    @ratio.setter
    def ratio(self, value: float):
        self._validator.validate_type(value, float).validate()

        self.__ratio = value

    @property
    def parent_unit(self):
        return self.__parent_unit

    @parent_unit.setter
    def parent_unit(self, value):
        self._validator.validate_type(value, MeasurementUnit).validate()

        self.__parent_unit = value

    def __get_primal_unit(self):
        primal_parent = deepcopy(self.parent_unit)
        total_ratio = self.ratio

        while primal_parent is not None:
            total_ratio *= primal_parent.ratio

            if primal_parent.parent_unit is None:
                break

            primal_parent = deepcopy(primal_parent.parent_unit)

        if primal_parent is None:
            return self

        primal_parent.ratio = total_ratio

        return primal_parent

    def inner_eq(self, other):
        if not isinstance(other, MeasurementUnit):
            return False

        primal_parent_self = self.__get_primal_unit()
        primal_parent_other = other.__get_primal_unit()

        return primal_parent_self.name == primal_parent_other.name and \
               primal_parent_self.ratio == primal_parent_other.ratio

    def __repr__(self):
        return f"{self.__name} {self.__ratio}"
