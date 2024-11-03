from src.core.domain.entity.storage_turnover import StorageTurnover
from src.core.util.helper.validator import Validator


class StorageTurnoverDataSource:

    __validator: Validator
    __data = {}
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(StorageTurnoverDataSource, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__data = {}
        self.__validator = Validator()

    def create(self, turnover: StorageTurnover):
        self.__validator.validate_type(turnover, StorageTurnover).validate()

        self.__data[turnover.id] = turnover

    def get_all(self) -> list[StorageTurnover]:
        return list(self.__data.values())

    def get_by_id(self, id: str) -> StorageTurnover | None:
        self.__validator.validate_type(id, str).validate()

        result = None

        if id in self.__data:
            result = self.__data[id]

        return result

    def create_multiple(self, turnovers: list[StorageTurnover]):
        self.__validator.validate_list_type(turnovers, StorageTurnover).validate()

        for turnover in turnovers:
            self.create(turnover)

    def delete(self, id: str):
        self.__validator.validate_type(id, str).validate()

        if id in self.__data:
            del self.__data[id]
