from .prototype import BasePrototype
from .filter import nomenclature, OperationEnum, MeasurementUnitFilter
from .filter.base import FilterEntry


class MeasurementUnitPrototype(BasePrototype):

    def create(self, filter_dto: MeasurementUnitFilter):
        super().create(filter_dto)

        data = self._name(filter_dto.name, self.data)

        data = self._id(filter_dto.id, data)

        return data