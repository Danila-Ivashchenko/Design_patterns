from datetime import datetime

from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.storage import Storage
from src.core.domain.entity.storage_turnover import StorageTurnover
from src.core.domain.enums.event_type import EventType
from src.core.domain.enums.operation_type import OperationEnum
from src.core.domain.repository.data.data_repository import DataRepository
from src.core.domain.repository.storage_transaction.repository import StorageTransactionRepository
from src.core.domain.repository.storage_turnover.repository import StorageTurnoverRepository
from src.core.domain.service.base.base import BaseService
from src.core.domain.service.dto.storage_turnover import StorageTurnoverDTO
from src.core.domain.service.filter import FilterService
from src.core.domain.service.setting_manager import SettingsManager
from src.core.util.observer.event import Event
from src.infrastructure.data.prototype.filter.entry.filter_entry import FilterEntry
from src.infrastructure.factory.filter import FilterFactory
from src.infrastructure.factory.prototipe import PrototypeFactory
from src.infrastructure.factory.storage_turnover import StorageTurnoverFactory


class StorageService(BaseService):

    __filter_service: FilterService
    __storage_turnover_factory: StorageTurnoverFactory
    __data_repository: DataRepository
    __storage_transaction_repository: StorageTurnoverRepository
    __storage_turnover_repository: StorageTurnoverRepository
    __settings_manager: SettingsManager

    def __init__(self, data_repository: DataRepository, filter_service: FilterService, settings_manager: SettingsManager):
        super().__init__()

        self._validator.validate_type(data_repository, DataRepository)
        self._validator.validate_type(filter_service, FilterService)
        self._validator.validate_type(settings_manager, SettingsManager)
        self._validator.validate()

        self.__data_repository = data_repository
        self.__filter_service = filter_service
        self.__storage_turnover_factory = StorageTurnoverFactory()

        self.__storage_turnover_repository = StorageTurnoverRepository()
        self.__storage_transaction_repository = StorageTransactionRepository()

        self.__settings_manager = settings_manager

    def update_turnovers_by_date_block(self, new_date_block: datetime):
        self._validator.validate_type(new_date_block, datetime).validate()

        date_block = self.__settings_manager.settings.date_block

        dto = StorageTurnoverDTO()
        dto.start_time = date_block
        dto.end_time = new_date_block

        new_turnovers = self.get_turnover(dto)
        old_turnovers = self.__storage_turnover_repository.find_all()

        merged_turnovers = self.__storage_turnover_factory.merge_turnovers(old_turnovers, new_turnovers)

        self.__storage_turnover_repository.create_multiple(merged_turnovers)

    def get_turnovers_with_start_time(self, dto: StorageTurnoverDTO) -> list[StorageTurnover]:
        self._validator.validate_type(dto, StorageTurnoverDTO).validate()

        all_transactions = self.__storage_transaction_repository.find_all()

        all_filters = [entry for entry in dto.filters]

        all_filters.append(FilterEntry("date_time", (dto.start_time, dto.end_time), OperationEnum.Between))

        transactions = self.__filter_service.get_storage_transactions_by_filters(all_transactions, all_filters)

        res = self.__storage_turnover_factory.create_turnovers(transactions)

        return res

    def get_turnovers_with_date_block(self, dto: StorageTurnoverDTO) -> list[StorageTurnover]:
        self._validator.validate_type(dto, StorageTurnoverDTO).validate()

        all_transactions = self.__storage_transaction_repository.find_all()

        all_filters = [entry for entry in dto.filters]

        date_block = self.__settings_manager.settings.date_block

        all_filters.append(FilterEntry("date_time", (date_block, dto.end_time), OperationEnum.Between))

        transactions = self.__filter_service.get_storage_transactions_by_filters(all_transactions, all_filters)
        turnovers = self.__storage_turnover_repository.find_all()

        filtered_turnovers = self.__filter_service.get_storage_turnovers_by_filters(turnovers, dto.filters)

        new_turnovers = self.__storage_turnover_factory.create_turnovers(transactions)

        merged_turnovers = self.__storage_turnover_factory.merge_turnovers(filtered_turnovers, new_turnovers)

        return merged_turnovers

    def get_turnover(self, dto: StorageTurnoverDTO) -> list[StorageTurnover]:
        res = []

        settings = self.__settings_manager.settings

        if dto.start_time == None:
            if dto.end_time > settings.date_block:
                res = self.get_turnovers_with_date_block(dto)
            else:
                dto.start_time = datetime.min
                res = self.get_turnovers_with_start_time(dto)
        else:
            res = self.get_turnovers_with_start_time(dto)


        return res

    def init_turnovers_by_date_block(self, date_block: datetime):
        self._validator.validate_type(date_block, datetime).validate()

        dto = StorageTurnoverDTO()
        dto.end_time = date_block

        turnovers = self.get_turnover(dto)

        self.__storage_turnover_repository.create_multiple(turnovers)

    def get_turnovers_by_date_block(self, date_block: datetime) -> list[StorageTurnover]:
        self._validator.validate_type(date_block, datetime).validate()

        return self.__storage_turnover_repository.find_all()

    def update_transactions_by_nomenclature(self, nomenclature: Nomenclature):
        self._validator.validate_type(nomenclature, Nomenclature).validate()

        transactions = self.__storage_transaction_repository.find_all()

        for transaction in transactions:
            if transaction.nomenclature == nomenclature:
                transaction.nomenclature = nomenclature
                self.__storage_transaction_repository.update(transaction)

    def update_turnovers_by_nomenclature(self, nomenclature: Nomenclature):
        self._validator.validate_type(nomenclature, Nomenclature).validate()

        turnovers = self.__storage_turnover_repository.find_all()

        for turnover in turnovers:
            if turnover.nomenclature == nomenclature:
                turnover.nomenclature = nomenclature
                self.__storage_turnover_repository.update(turnover)

    def handle_event(self, event: Event):
        super().handle_event(event)

        if event.type == EventType.CHANGE_NOMENCLATURE:
            nomenclature = event.payload

            self.update_transactions_by_nomenclature(nomenclature)
            self.update_turnovers_by_nomenclature(nomenclature)

        pass