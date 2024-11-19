from src.core.domain.entity.storage_transaction import StorageTransaction
from src.core.domain.repository.base.base import BaseRepository
from src.core.domain.repository.storage_transaction.data_source import StorageTransactionDataSource


class StorageTransactionRepository(BaseRepository):

    __data_source: StorageTransactionDataSource = StorageTransactionDataSource()
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(StorageTransactionRepository, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        super().__init__()

    def create(self, data: StorageTransaction) -> StorageTransaction:
        self._validator.validate_type(data, StorageTransaction).validate()

        return self.__data_source.create(data)

    def create_multiple(self, data: list[StorageTransaction]):
        self._validator.validate_list_type(data, StorageTransaction).validate()

        return self.__data_source.create_multiple(data)

    def update(self, data: StorageTransaction) -> StorageTransaction:
        self._validator.validate_type(data, StorageTransaction).validate()

        return self.__data_source.create(data)

    def update_multiple(self, data: list[StorageTransaction]) -> list[StorageTransaction]:
        self._validator.validate_list_type(data, StorageTransaction).validate()

        return self.__data_source.create_multiple(data)

    def find_by_id(self, id: str) -> StorageTransaction | None:
        self._validator.validate_type(id, str).validate()

        return self.__data_source.get_by_id(id)

    def find_all(self) -> list[StorageTransaction]:
        return self.__data_source.get_all()

    def delete(self, id: str) -> None:
        self._validator.validate_type(id, str).validate()

        self.__data_source.delete(id)

    def dump_json(self):
        result = self._json_helper.to_serialize(self.find_all())

        return result