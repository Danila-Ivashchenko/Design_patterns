from .prototype import BasePrototype
from .filter import nomenclature, OperationEnum, RecipeFilter
from .filter.base import FilterEntry


class RecipePrototype(BasePrototype):

    def create(self, filter_dto: RecipeFilter):
        super().create(filter_dto)

        data = self._name(filter_dto.name, self.data)
        data = self._id(filter_dto.id, data)

        return data