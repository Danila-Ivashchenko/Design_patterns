from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.storage_turnover import StorageTurnover
from src.core.util.helper.validator import Validator


class NomenclatureDataSource:

    __validator: Validator
    __data = {}
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(NomenclatureDataSource, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__validator = Validator()

    def create(self, nomenclature: Nomenclature) -> Nomenclature:
        self.__validator.validate_type(nomenclature, Nomenclature).validate()

        self.__data[nomenclature.id] = nomenclature

        return nomenclature

    def get_all(self) -> list[Nomenclature]:
        return list(self.__data.values())

    def get_by_id(self, id: str) -> Nomenclature | None:
        self.__validator.validate_type(id, str).validate()

        result = None

        if id in self.__data:
            result = self.__data[id]

        return result

    def create_multiple(self, nomenclatures: list[Nomenclature]) -> list[Nomenclature]:
        self.__validator.validate_list_type(nomenclatures, Nomenclature).validate()

        result = []

        for nomenclature in nomenclatures:
            result.append(self.create(nomenclature))

        return result

    def delete(self, id: str):
        self.__validator.validate_type(id, str).validate()

        if id in self.__data:
            del self.__data[id]
