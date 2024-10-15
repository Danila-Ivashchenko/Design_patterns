from src.infrastructure.data.prototype.prototype.base import BasePrototype
from src.infrastructure.data.prototype.filter.filter.recipe import RecipeFilter


class RecipePrototype(BasePrototype):

    def create(self, filter_dto: RecipeFilter):
        super().create(filter_dto)

        data = self._name(filter_dto.name, self.data)
        data = self._id(filter_dto.id, data)

        return data