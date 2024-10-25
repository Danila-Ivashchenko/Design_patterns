from datetime import datetime

from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.storage import Storage
from src.core.domain.entity.storage_turnover import StorageTurnover
from src.core.domain.enums.operation_type import OperationEnum
from src.core.domain.repository.data.data_repository import DataRepository
from src.core.domain.service.base.base import BaseService
from src.core.domain.service.dto.storage_turnover import StorageTurnoverDTO
from src.core.domain.service.filter import FilterService
from src.infrastructure.data.prototype.filter.entry.filter_entry import FilterEntry
from src.infrastructure.factory.filter import FilterFactory
from src.infrastructure.factory.prototipe import PrototypeFactory
from src.infrastructure.factory.storage_turnover import StorageTurnoverFactory


class StorageService(BaseService):

    __filter_service: FilterService
    __storage_turnover_factory: StorageTurnoverFactory
    __data_repository: DataRepository

    def __init__(self, data_repository: DataRepository, filter_service: FilterService):
        super().__init__()

        self._validator.validate_type(data_repository, DataRepository)
        self._validator.validate_type(filter_service, FilterService)
        self._validator.validate()

        self.__data_repository = data_repository
        self.__filter_service = filter_service
        self.__storage_turnover_factory = StorageTurnoverFactory()

    def get_turnover(self, dto: StorageTurnoverDTO) -> list[StorageTurnover]:
        self._validator.validate_type(dto, StorageTurnoverDTO).validate()

        all_transactions = self.__data_repository.data[DataRepository.storage_transaction_key()]

        all_filters = [entry for entry in dto.filters]

        all_filters.append(FilterEntry("date_time", (dto.start_time, dto.end_time), OperationEnum.Between))

        transactions = self.__filter_service.get_storage_transactions_by_filters(all_transactions, all_filters)

        res = self.__storage_turnover_factory.create_turnovers(transactions, dto.start_time, dto.end_time)

        return res
