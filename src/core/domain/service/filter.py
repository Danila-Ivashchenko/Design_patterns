from src.core.domain.entity.measurement_unit import MeasurementUnit
from src.core.domain.entity.recipe import Recipe
from src.core.domain.entity.storage import Storage
from src.core.domain.entity.storage_transaction import StorageTransaction
from src.core.domain.entity.storage_turnover import StorageTurnover
from src.core.domain.enums.event_type import EventType
from src.core.domain.enums.operation_type import OperationEnum
from src.core.domain.service.base.base import BaseService
from src.core.util.observer.event import Event
from src.infrastructure.data.generator.measurement_unit import MeasurementUnitGenerator
from src.infrastructure.data.prototype.filter.entry.filter_entry import FilterEntry
from src.infrastructure.factory.filter import FilterFactory
from src.infrastructure.factory.prototipe import PrototypeFactory
from src.core.domain.errors.abstract import AbstractException


class FilterService(BaseService):

    __filter_factory: FilterFactory
    __prototype_factory: PrototypeFactory

    def __init__(self, filter_factory: FilterFactory, prototype_factory: PrototypeFactory):
        super().__init__()

        self._validator.validate_type(filter_factory, FilterFactory)
        self._validator.validate_type(prototype_factory, PrototypeFactory)
        self._validator.validate()

        self.__filter_factory = filter_factory
        self.__prototype_factory = prototype_factory

    def get_by_entity_and_fiter_data(self, data: list, entity_name: str, filter_data: list):
        self._validator.validate_type(entity_name, str).validate_type(filter_data, list)
        self._validator.validate_type(data, list)

        try:
            self._validator.validate()

            filter_dto = self.__filter_factory.create_filter(entity_name, filter_data)
            prototype = self.__prototype_factory.create_prototype(entity_name, data)

            return prototype.create(filter_dto)
        except AbstractException as e:
            self.set_error(e)

    def __get_by_entity_and_filters(self, data: list, entity_name: str, filters: list[FilterEntry]) -> list:
        prototype = self.__prototype_factory.create_prototype(entity_name, data)
        return prototype.create(filters)

    def get_storage_by_id(self, id: str, data: list[Storage]) -> Storage | None:
        self._validator.validate_type(id, str)
        self._validator.validate_list_type(data, Storage)
        self._validator.validate()

        storages = self.__get_by_entity_and_filters(data, "storage", [FilterEntry("id", id, OperationEnum.Equal)])

        if len(storages) == 0:
            return None

        return storages[0]

    def get_storage_transactions_by_filters(self, data: list[StorageTransaction], filters: list[FilterEntry]) -> list[StorageTransaction]:
        self._validator.validate_list_type(data, StorageTransaction)
        self._validator.validate_list_type(filters, FilterEntry)
        self._validator.validate()

        return self.__get_by_entity_and_filters(data, "storage_transaction", filters)

    def get_storage_turnovers_by_filters(self, data: list[StorageTurnover], filters: list[FilterEntry]) -> list[StorageTurnover]:
        self._validator.validate_list_type(data, StorageTurnover)
        self._validator.validate_list_type(filters, FilterEntry)
        self._validator.validate()

        return self.__get_by_entity_and_filters(data, "storage_turnover", filters)

    def get_measurement_units_by_filters(self, data: list[MeasurementUnit], filters: list[FilterEntry]) -> list[MeasurementUnit]:
        self._validator.validate_list_type(data, MeasurementUnit)
        self._validator.validate_list_type(filters, FilterEntry)
        self._validator.validate()

        return self.__get_by_entity_and_filters(data, "measurement_unit", filters)

    def get_recipes_by_filters(self, data: list[Recipe], filters: list[FilterEntry]) -> list[Recipe]:
        self._validator.validate_list_type(data, Recipe)
        self._validator.validate_list_type(filters, FilterEntry)
        self._validator.validate()

        return self.__get_by_entity_and_filters(data, "recipe", filters)

    def handle_event(self, event: Event):
        super().handle_event(event)

        pass


