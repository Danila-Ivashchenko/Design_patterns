import datetime
import unittest as un

from src.core.domain.entity.measurement_unit import MeasurementUnit
from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.storage import Storage
from src.core.domain.entity.storage_transaction import StorageTransaction
from src.core.domain.enums.storage_transaction_type import StorageTransactionType
from src.infrastructure.data.generator.storage_transaction import StorageTransactionGenerator


class TestStorageTransactionGenerator(un.TestCase):
    def test_generate(self):

        # Arrange
        generator = StorageTransactionGenerator()

        # Act

        items = generator.list

        # Assert

        for item in items:
            assert isinstance(item, StorageTransaction)
            assert isinstance(item.nomenclature, Nomenclature)
            assert isinstance(item.storage, Storage)
            assert isinstance(item.measurement_unit, MeasurementUnit)
            assert isinstance(item.count, float)
            assert isinstance(item.type, StorageTransactionType)
            assert isinstance(item.date_time, datetime.datetime)
