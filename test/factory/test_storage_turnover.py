import unittest as un
from datetime import datetime

from src.core.domain.enums.operation_type import OperationEnum
from src.core.domain.repository.data.data_repository import DataRepository
from src.core.domain.service.dto.storage_turnover import StorageTurnoverDTO
from src.core.domain.service.filter import FilterService
from src.core.domain.service.start import StartService
from src.core.domain.service.storage import StorageService
from src.infrastructure.data.prototype.filter.entry.filter_entry import FilterEntry
from src.infrastructure.factory.filter import FilterFactory
from src.infrastructure.factory.prototipe import PrototypeFactory

filter_factory = FilterFactory()
prototype_factory = PrototypeFactory()

data_repository = DataRepository()

start_service = StartService(data_repository)
filter_service = FilterService(filter_factory, prototype_factory)
storage_service = StorageService(data_repository, filter_service)


class TestStorageTurnover(un.TestCase):
    def test_storage_turnover(self):
        # Arrange

        dto = StorageTurnoverDTO()

        dto.start_time = datetime.fromtimestamp(1729740000)
        dto.end_time = datetime.fromtimestamp(1729743600)
        dto.filters = [FilterEntry("nomenclature.name", "мясо", OperationEnum.Equal)]

        # Act

        res = storage_service.get_turnover(dto)

        # Assert

        assert res is not None

        assert len(res) > 0

        for item in res:
            assert item.nomenclature.name == "мясо"
            assert item.start_date == dto.start_time
            assert item.end_date == dto.end_time
            assert item.amount != 0
