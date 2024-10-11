from .base.prototype import BasePrototype
from .filter import nomenclature, OperationEnum, MeasurementUnitFilter
from .filter.base import FilterEntry


class MeasurementUnitPrototype(BasePrototype):

    def create(self, filter_dto: MeasurementUnitFilter):
        super().create(filter_dto)

        data = self.__name(filter_dto.name, self.data)
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
                continue

            parent = item.parent_unit
            while parent != None:
                if operation(parent.name, name.value):
                    res.append(item)
                    break
                parent = parent.parent_unit

        return res

    def __id(self, id: FilterEntry, data: list):
        if id == None:
            return data

        operation = self._operation_mapper.enum_to_operation(id.operation)
        res = []

        for item in data:
            if operation(item.id, id.value):
                res.append(item)
                continue

            parent = item.parent_unit
            while parent != None:
                if operation(parent.id, id.value):
                    res.append(item)
                    break
                parent = parent.parent_unit

        return res