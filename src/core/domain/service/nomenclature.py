from src.core.domain.entity.measurement_unit import MeasurementUnit
from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.recipe import Recipe
from src.core.domain.entity.storage_transaction import StorageTransaction
from src.core.domain.enums.event_type import EventType
from src.core.domain.enums.operation_type import OperationEnum
from src.core.domain.errors.is_used import IsUsedException
from src.core.domain.errors.not_found import NotFoundException
from src.core.domain.repository.data.data_repository import DataRepository
from src.core.domain.repository.measurement_unit.repository import MeasurementUnitRepository
from src.core.domain.repository.nomenclature.repository import NomenclatureRepository
from src.core.domain.repository.recipe.repository import RecipeRepository
from src.core.domain.service.base.base import BaseService
from src.core.domain.service.dto.nomenclature.create import CreateNomenclatureDTO
from src.core.domain.service.dto.nomenclature.update import UpdateNomenclatureDTO
from src.core.domain.service.filter import FilterService
from src.core.util.observer.event import Event
from src.di.observer import observer

from src.infrastructure.data.prototype.filter.entry.filter_entry import FilterEntry


class NomenclatureService(BaseService):

    __filter_service: FilterService
    __nomenclature_repository: NomenclatureRepository
    __recipe_repository: RecipeRepository
    __measurement_unit_repository: MeasurementUnitRepository
    __data_repository: DataRepository

    # to provide singleton
    __instance = None

    def __new__(cls, filter_service: FilterService):
        if cls.__instance is None:
            cls.__instance = super(NomenclatureService, cls).__new__(cls)

        return cls.__instance

    def __init__(self, filter_service: FilterService):
        super().__init__()

        self.__filter_service = filter_service
        self.__nomenclature_repository = NomenclatureRepository()
        self.__recipe_repository = RecipeRepository()
        self.__measurement_unit_repository = MeasurementUnitRepository()

        self.__data_repository = DataRepository()

    def get_all(self) -> list[Nomenclature]:
        return self.__nomenclature_repository.find_all()

    def get_by_id(self, id: str) -> Nomenclature | None:
        return self.__nomenclature_repository.find_by_id(id)

    def create(self, data: CreateNomenclatureDTO) -> Nomenclature:
        nomenclature = Nomenclature()

        measurement_unit = self.__find_measurement_unit(data.measurement_unit_id)

        nomenclature.name = data.name
        nomenclature.nomenclature_group_id = data.nomenclature_group_id
        nomenclature.measurement_unit = measurement_unit

        return self.__nomenclature_repository.create(nomenclature)

    def update(self, data: UpdateNomenclatureDTO) -> Nomenclature | None:
        found = self.__nomenclature_repository.find_by_id(data.id)

        if found is None:
            return NotFoundException.not_found_entity_by_id("nomenclature", data.id)

        if data.measurement_unit_id != None:
            measurement_unit = self.__find_measurement_unit(data.measurement_unit_id)

            if measurement_unit is None:
                return NotFoundException.not_found_measurement_unit(data.measurement_unit_id)

            found.measurement_unit = measurement_unit

        if data.name != None:
            found.name = data.name

        if data.nomenclature_group_id != None:
            found.nomenclature_group_id = data.nomenclature_group_id

        result = self.__nomenclature_repository.update(found)

        observer.notify(EventType.CHANGE_NOMENCLATURE, found)

        return result

    def delete(self, id: str):
        self._validator.validate_type(id, str).validate()

        found = self.__nomenclature_repository.find_by_id(id)

        if found is None:
            raise NotFoundException.not_found_entity_by_id("nomenclature", id)

        if self.__check_nomenclature_used(id):
            raise IsUsedException.used_entity_by_id("nomenclature", id)

        self.__nomenclature_repository.delete(id)

    def __check_nomenclature_used(self, id: str):
        recipes = self.__find_recipe_by_nomenclature_id(id)
        storage_transactions = self.__find_storage_transaction_by_nomenclature_id(id)

        return len(recipes) > 0 or len(storage_transactions) > 0

    def __find_recipe_by_nomenclature_id(self, id: str) -> list[Recipe]:
        all_measurement_units = self.__recipe_repository.find_all()

        filter = FilterEntry()

        filter.key = "ingredients.nomenclature.id"
        filter.operation = OperationEnum.Equal
        filter.value = id

        result = self.__filter_service.get_recipes_by_filters(all_measurement_units, [filter])

        return result

    def __find_storage_transaction_by_nomenclature_id(self, id: str) -> list[StorageTransaction]:
        all_measurement_units = self.__data_repository.data[DataRepository.storage_transaction_key()]

        filter = FilterEntry()

        filter.key = "nomenclature.id"
        filter.operation = OperationEnum.Equal
        filter.value = id

        result = self.__filter_service.get_storage_transactions_by_filters(all_measurement_units, [filter])

        return result

    def __find_measurement_unit(self, id: str) -> MeasurementUnit | None:
        return self.__measurement_unit_repository.find_by_id(id)

    def handle_event(self, event: Event):
        super().handle_event(event)

        pass