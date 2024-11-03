import unittest as un
from datetime import datetime, timedelta

from main import update_date_block
from src.core.domain.enums.operation_type import OperationEnum
from src.core.domain.repository.data.data_repository import DataRepository
from src.core.domain.service.dto.storage_turnover import StorageTurnoverDTO
from src.core.domain.service.dto.update_date_block_dto import UpdateDateBlockDTO
from src.core.domain.service.filter import FilterService
from src.core.domain.service.setting_manager import SettingsManager
from src.core.domain.service.start import StartService
from src.core.domain.service.storage import StorageService
from src.infrastructure.data.prototype.filter.entry.filter_entry import FilterEntry
from src.infrastructure.factory.filter import FilterFactory
from src.infrastructure.factory.prototipe import PrototypeFactory

filter_factory = FilterFactory()
prototype_factory = PrototypeFactory()
setting_manager = SettingsManager()

setting_manager.open('json/settings.json')

data_repository = DataRepository()

start_service = StartService(data_repository)
filter_service = FilterService(filter_factory, prototype_factory)
storage_service = StorageService(data_repository, filter_service, setting_manager)


class TestStorageTurnover(un.TestCase):
    def test_storage_turnover(self):
        # Arrange

        dto = StorageTurnoverDTO()

        dto.start_time = datetime.fromtimestamp(1730426400)
        dto.end_time = datetime.fromtimestamp(1731254400)
        dto.filters = [FilterEntry("nomenclature.name", "мясо", OperationEnum.Equal)]

        # Act

        res = storage_service.get_turnover(dto)

        # Assert

        assert res is not None

        assert len(res) > 0

        for item in res:
            assert item.nomenclature.name == "мясо"
            assert item.amount != 0


    def test_with_date_block(self):
        # Arrange

        new_date_block = datetime.fromtimestamp(1730390400)

        update_date_block_dto = UpdateDateBlockDTO()
        update_date_block_dto.value = new_date_block

        setting_manager.update_date_block(update_date_block_dto)

        settings = setting_manager.settings

        storage_service.init_turnovers_by_date_block(settings.date_block)

        dto = StorageTurnoverDTO()

        dto.end_time = settings.date_block + timedelta(days=5)

        # Act
        start = datetime.now()
        res_1 = storage_service.get_turnover(dto)
        end = datetime.now()

        print(f"Time with date block: {settings.date_block} and dto.end_time: {dto.end_time}: {end - start}")

        new_date_block = settings.date_block + timedelta(days=1)
        storage_service.update_turnovers_by_date_block(new_date_block)

        update_date_block_dto = UpdateDateBlockDTO()
        update_date_block_dto.value = new_date_block

        setting_manager.update_date_block(update_date_block_dto)

        new_start = datetime.now()
        res_2 = storage_service.get_turnover(dto)
        new_end = datetime.now()

        print(f"Time with date block: {settings.date_block} and dto.end_time: {dto.end_time}: {new_end - new_start}")

        new_date_block = settings.date_block + timedelta(days=2)
        storage_service.update_turnovers_by_date_block(new_date_block)

        update_date_block_dto = UpdateDateBlockDTO()
        update_date_block_dto.value = new_date_block

        setting_manager.update_date_block(update_date_block_dto)

        new_start = datetime.now()
        res_3 = storage_service.get_turnover(dto)
        new_end = datetime.now()

        print(f"Time with date block: {settings.date_block} and dto.end_time: {dto.end_time}: {new_end - new_start}")

        # Assert

        assert len(res_1) == len(res_2) == len(res_3)

        for i in range(len(res_1)):
            assert res_1[i].measurement_unit == res_2[i].measurement_unit == res_3[i].measurement_unit

            assert res_1[i].nomenclature == res_2[i].nomenclature == res_3[i].nomenclature

            assert res_1[i].amount == res_2[i].amount == res_3[i].amount

            assert res_1[i].storage == res_2[i].storage == res_3[i].storage

