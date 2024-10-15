from .prototype import BasePrototype
from .filter import nomenclature, OperationEnum, NomenclatureGroupFilter
from .filter.base import FilterEntry


class NomenclatureGroupPrototype(BasePrototype):

    def create(self, filter_dto: NomenclatureGroupFilter):
        super().create(filter_dto)

        data = self._name(filter_dto.name, self.data)

        data = self._id(filter_dto.id, data)

        return data

