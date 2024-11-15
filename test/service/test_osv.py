import unittest as un
import datetime

from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.osv import Osv
from src.core.domain.entity.storage import Storage
from src.core.domain.repository.data.data_repository import DataRepository
from src.core.domain.service.dto.osv.get import OsvGetDTO
from src.core.domain.service.filter import FilterService
from src.core.domain.service.osv import OsvService
from src.core.domain.service.setting_manager import SettingsManager
from src.core.domain.service.start import StartService
from src.core.domain.service.storage import StorageService

from src.infrastructure.factory.filter import FilterFactory
from src.infrastructure.factory.prototipe import PrototypeFactory

data_repository = DataRepository()

settings_manager = SettingsManager()

settings_manager.open("/json/settings_1.json")

start_service = StartService(data_repository)

filter_factory = FilterFactory()
prototype_factory = PrototypeFactory()

filter_service = FilterService(filter_factory, prototype_factory)

storage_service = StorageService(data_repository, filter_service, settings_manager)

osv_service = OsvService(filter_service, storage_service)


class TestOsvService(un.TestCase):
    def test_get(self):
        #Arrange

        dto = OsvGetDTO()

        dto.start_date = 1730426400
        dto.end_date = 1730635200

        #Act

        data = osv_service.get(dto)

        #Assert

        assert data is not None

        assert len(data) > 0

        for item in data:
            assert isinstance(item, Osv)
            assert isinstance(item.start_date, datetime.datetime)
            assert isinstance(item.end_date, datetime.datetime)
            assert isinstance(item.amount_at_start, float)
            assert isinstance(item.amount_at_end, float)

            assert isinstance(item.nomenclature, Nomenclature)
            assert isinstance(item.storage, Storage)
