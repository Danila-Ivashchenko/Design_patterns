from src.core.domain.entity.storage import Storage
from src.core.domain.repository.base.base import BaseRepository
from src.core.domain.repository.storage.data_source import StorageDataSource


class StorageRepository(BaseRepository):

    __data_source: StorageDataSource = StorageDataSource()
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(StorageRepository, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        super().__init__()

    def create(self, data: Storage) -> Storage:
        self._validator.validate_type(data, Storage).validate()

        return self.__data_source.create(data)

    def create_multiple(self, data: list[Storage]):
        self._validator.validate_list_type(data, Storage).validate()

        return self.__data_source.create_multiple(data)

    def update(self, data: Storage) -> Storage:
        self._validator.validate_type(data, Storage).validate()

        return self.__data_source.create(data)

    def update_multiple(self, data: list[Storage]) -> list[Storage]:
        self._validator.validate_list_type(data, Storage).validate()

        return self.__data_source.create_multiple(data)

    def find_by_id(self, id: str) -> Storage | None:
        self._validator.validate_type(id, str).validate()

        return self.__data_source.get_by_id(id)

    def find_all(self) -> list[Storage]:
        return self.__data_source.get_all()

    def delete(self, id: str) -> None:
        self._validator.validate_type(id, str).validate()

        self.__data_source.delete(id)

    def dump_json(self):
        result = self._json_helper.to_serialize(self.find_all())

        return result