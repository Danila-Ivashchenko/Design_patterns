from src.core.domain.entity.nomenclature_group import NomenclatureGroup
from src.core.domain.repository.base.base import BaseRepository
from src.core.domain.repository.nomenclature_group.data_source import NomenclatureGroupDataSource


class NomenclatureGroupRepository(BaseRepository):
    __instance = None
    __data_source: NomenclatureGroupDataSource = NomenclatureGroupDataSource()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(NomenclatureGroupRepository, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        super().__init__()

    def create(self, data: NomenclatureGroup) -> NomenclatureGroup:
        self._validator.validate_type(data, NomenclatureGroup).validate()

        return self.__data_source.create(data)

    def create_multiple(self, data: list[NomenclatureGroup]):
        self._validator.validate_list_type(data, NomenclatureGroup).validate()

        return self.__data_source.create_multiple(data)

    def update(self, data: NomenclatureGroup) -> NomenclatureGroup:
        self._validator.validate_type(data, NomenclatureGroup).validate()

        return self.__data_source.create(data)

    def update_multiple(self, data: list[NomenclatureGroup]) -> list[NomenclatureGroup]:
        self._validator.validate_list_type(data, NomenclatureGroup).validate()

        return self.__data_source.create_multiple(data)

    def find_by_id(self, id: str) -> NomenclatureGroup | None:
        self._validator.validate_type(id, str).validate()

        return self.__data_source.get_by_id(id)

    def find_all(self) -> list[NomenclatureGroup]:
        return self.__data_source.get_all()

    def delete(self, id: str) -> None:
        self._validator.validate_type(id, str).validate()

        self.__data_source.delete(id)

    def dump_json(self):
        result = self._json_helper.to_serialize(self.find_all())

        return result