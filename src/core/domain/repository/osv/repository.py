from src.core.domain.entity.osv import Osv
from src.core.domain.repository.base.base import BaseRepository
from src.core.domain.repository.osv.data_source import OsvDataSource


class OsvRepository(BaseRepository):
    __instance = None
    __data_source: OsvDataSource = OsvDataSource()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(OsvRepository, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        super().__init__()

    def create(self, data: Osv) -> Osv:
        self._validator.validate_type(data, Osv).validate()

        return self.__data_source.create(data)

    def create_multiple(self, data: list[Osv]):
        self._validator.validate_list_type(data, Osv).validate()

        return self.__data_source.create_multiple(data)

    def update(self, data: Osv) -> Osv:
        self._validator.validate_type(data, Osv).validate()

        return self.__data_source.create(data)

    def update_multiple(self, data: list[Osv]) -> list[Osv]:
        self._validator.validate_list_type(data, Osv).validate()

        return self.__data_source.create_multiple(data)

    def find_by_id(self, id: str) -> Osv | None:
        self._validator.validate_type(id, str).validate()

        return self.__data_source.get_by_id(id)

    def find_all(self) -> list[Osv]:
        return self.__data_source.get_all()

    def delete(self, id: str) -> None:
        self._validator.validate_type(id, str).validate()

        self.__data_source.delete(id)

    def dump_json(self):
        result = self._json_helper.to_serialize(self.find_all())

        return result