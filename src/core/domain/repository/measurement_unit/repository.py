from src.core.domain.entity.measurement_unit import MeasurementUnit
from src.core.domain.repository.base.base import BaseRepository
from src.core.domain.repository.measurement_unit.data_source import MeasurementUnitDataSource


class MeasurementUnitRepository(BaseRepository):
    __instance = None
    __data_source: MeasurementUnitDataSource = MeasurementUnitDataSource()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(MeasurementUnitRepository, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        super().__init__()

    def create(self, data: MeasurementUnit) -> MeasurementUnit:
        self._validator.validate_type(data, MeasurementUnit).validate()

        return self.__data_source.create(data)

    def create_multiple(self, data: list[MeasurementUnit]):
        self._validator.validate_list_type(data, MeasurementUnit).validate()

        return self.__data_source.create_multiple(data)

    def update(self, data: MeasurementUnit) -> MeasurementUnit:
        self._validator.validate_type(data, MeasurementUnit).validate()

        return self.__data_source.create(data)

    def update_multiple(self, data: list[MeasurementUnit]) -> list[MeasurementUnit]:
        self._validator.validate_list_type(data, MeasurementUnit).validate()

        return self.__data_source.create_multiple(data)

    def find_by_id(self, id: str) -> MeasurementUnit | None:
        self._validator.validate_type(id, str).validate()

        return self.__data_source.get_by_id(id)

    def find_all(self) -> list[MeasurementUnit]:
        return self.__data_source.get_all()

    def delete(self, id: str) -> None:
        self._validator.validate_type(id, str).validate()

        self.__data_source.delete(id)

    def dump_json(self):
        result = self._json_helper.to_serialize(self.find_all())

        return result
