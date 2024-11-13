from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.storage_turnover import StorageTurnover
from src.core.domain.repository.base.base import BaseRepository
from src.core.domain.repository.nomenclature.data_source import NomenclatureDataSource
from src.core.domain.repository.storage_turnover.data_source import StorageTurnoverDataSource


class NomenclatureRepository(BaseRepository):
    __instance = None
    __data_source: NomenclatureDataSource = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(NomenclatureRepository, cls).__new__(cls)
            cls.__data_source = NomenclatureDataSource()
        return cls.__instance

    def __init__(self):
        super().__init__()

        self.__data_source = NomenclatureDataSource()

    def create(self, data: Nomenclature) -> Nomenclature:
        self._validator.validate_type(data, Nomenclature).validate()

        return self.__data_source.create(data)

    def create_multiple(self, data: list[Nomenclature]):
        self._validator.validate_list_type(data, Nomenclature).validate()

        self.__data_source.create_multiple(data)

    def update(self, data: Nomenclature) -> Nomenclature:
        self._validator.validate_type(data, Nomenclature).validate()

        return self.__data_source.create(data)

    def update_multiple(self, data: list[Nomenclature]) -> list[Nomenclature]:
        self._validator.validate_list_type(data, StorageTurnover).validate()

        return self.__data_source.create_multiple(data)

    def find_by_id(self, id: str) -> Nomenclature | None:
        self._validator.validate_type(id, str).validate()

        return self.__data_source.get_by_id(id)

    def find_all(self) -> list[Nomenclature]:
        return self.__data_source.get_all()

    def delete(self, id: str) -> None:
        self._validator.validate_type(id, str).validate()

        self.__data_source.delete(id)

    def dump_json(self):
        result = self._json_helper.to_serialize(self.find_all())

        return result
