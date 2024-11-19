from src.core.domain.entity.osv import Osv
from src.core.domain.entity.storage_turnover import StorageTurnover
from src.core.domain.enums.operation_type import OperationEnum
from src.core.domain.repository.nomenclature.repository import NomenclatureRepository
from src.core.domain.repository.storage.repository import StorageRepository
from src.core.domain.service.base.base import BaseService
from src.core.domain.service.dto.osv.get import OsvGetDTO
from src.core.domain.service.dto.storage_turnover import StorageTurnoverDTO
from src.core.domain.service.filter import FilterService
from src.core.domain.service.storage import StorageService
from src.infrastructure.data.prototype.filter.entry.filter_entry import FilterEntry
from src.infrastructure.factory.osv import OsvFactory, CreateOsvFactoryDTO
from src.infrastructure.factory.storage_turnover import StorageTurnoverFactory


class OsvService(BaseService):

    __filter_service: FilterService
    __storage_service: StorageService

    __nomenclature_repository: NomenclatureRepository
    __storage_repository: StorageRepository

    __turnover_factory: StorageTurnoverFactory
    __osv_factory: OsvFactory
    # to provide singleton
    __instance = None

    def __new__(cls, filter_service: FilterService, storage_service: StorageService):
        if cls.__instance is None:
            cls.__instance = super(OsvService, cls).__new__(cls)

        return cls.__instance

    def __init__(self, filter_service: FilterService, storage_service: StorageService):
        super().__init__()

        self.__filter_service = filter_service
        self.__storage_service = storage_service

        self.__turnover_factory = StorageTurnoverFactory()
        self.__osv_factory = OsvFactory()

        self.__nomenclature_repository = NomenclatureRepository()
        self.__storage_repository = StorageRepository()

    def get(self, dto: OsvGetDTO) -> list[Osv]:

        filters = []

        if dto.storage_id is not None:
            filters.append(FilterEntry("storage.id", dto.storage_id, OperationEnum.Equal))

        start_turnovers_dto = StorageTurnoverDTO()
        start_turnovers_dto.end_time = dto.start_date
        start_turnovers_dto.filters = filters

        turnovers_to_start = self.__storage_service.get_turnover(start_turnovers_dto)

        end_turnovers_dto = StorageTurnoverDTO()
        end_turnovers_dto.start_time = dto.start_date
        end_turnovers_dto.end_time = dto.end_date
        end_turnovers_dto.filters = filters

        turnovers_from_start_to_end = self.__storage_service.get_turnover(end_turnovers_dto)

        turnovers_to_end = self.__turnover_factory.merge_turnovers(turnovers_from_start_to_end, turnovers_to_start)

        all_nomenclatures = self.__nomenclature_repository.find_all()

        storages = []

        if dto.storage_id is not None:
            storage = self.__storage_repository.find_by_id(dto.storage_id)

            storages.append(storage)
        else:
            storages = self.__storage_repository.find_all()


        factory_dto = CreateOsvFactoryDTO()

        factory_dto.turnovers_to_end = turnovers_to_end
        factory_dto.turnovers_to_start = turnovers_to_start

        factory_dto.storages = storages
        factory_dto.nomenclatures = all_nomenclatures

        factory_dto.start_date = dto.start_date
        factory_dto.end_date = dto.end_date

        result = self.__osv_factory.from_storage_turnovers(factory_dto)

        return result

