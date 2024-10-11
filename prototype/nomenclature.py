from .base.prototype import BasePrototype
from .filter import nomenclature, OperationEnum, NomenclatureFilter
from .filter.base import FilterEntry


class NomenclaturePrototype(BasePrototype):

    def create(self, filter_dto: NomenclatureFilter):
        super().create(filter_dto)

        data = self.__name(filter_dto.name, self.data)
        print("here")
        data = self.__id(filter_dto.id, data)

        return data

    def __name(self, name: FilterEntry, data: list):
        if name == None:
            return data

        operation = self._operation_mapper.enum_to_operation(name.operation)
        res = []

        for item in data:
            if operation(item.name, name.value):
                res.append(item)

        return res

    def __id(self, id: FilterEntry, data: list):
        if id == None:
            print(data)
            return data

        operation = self._operation_mapper.enum_to_operation(id.operation)
        res = []

        for item in data:
            if operation(item.id, id.value):
                res.append(item)

        return res