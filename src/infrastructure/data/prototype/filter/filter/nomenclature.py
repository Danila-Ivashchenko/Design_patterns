from src.infrastructure.data.prototype.filter.filter.base import Filter
from src.infrastructure.data.prototype.filter.entry.filter_entry import FilterEntry
from src.core.domain.enums.operation_type import OperationEnum
from src.core.domain.abstract.typed_none import typed_none



class NomenclatureFilter(Filter):

    __name: FilterEntry = None
    __id: FilterEntry = None

    # def __init__(self, name: str = "", id: str = ""):
    #     self.__name = name
    #     self.__id = id

    @property
    @typed_none(FilterEntry)
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: FilterEntry):
        self.__name = value

    def name_operation(self, operation: OperationEnum):
        self.__name.operation = operation

    @property
    @typed_none(FilterEntry)
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: FilterEntry):
        self.__id = value

    def id_operation(self, operation: OperationEnum):
        self.__id.operation = operation