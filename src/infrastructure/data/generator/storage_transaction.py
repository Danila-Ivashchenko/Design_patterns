from datetime import datetime

from src.core.domain.entity.measurement_unit import MeasurementUnit
from src.core.domain.entity.storage_transaction import StorageTransaction
from src.core.domain.enums.storage_transaction_type import StorageTransactionType
from src.infrastructure.data.generator.base import BaseGenerator
from src.infrastructure.data.generator.measurement_unit import MeasurementUnitGenerator
from src.infrastructure.data.generator.nomenclature import NomenclatureGenerator
from src.infrastructure.data.generator.storage import StorageGenerator


class StorageTransactionGenerator(BaseGenerator):

    def __init__(self):
        super().__init__()

        self.__storage_generator = StorageGenerator()
        self.__nomenclature_generator = NomenclatureGenerator()
        self.__measurement_unit_generator = MeasurementUnitGenerator()

        self.__generate()

    def __generate(self):

        self.__generate_egs_arrival()
        self.__generate_egs_consumption()
        self.__generate_milk_arrival()
        self.__generate_milk_consumption()
        self.__generate_meat_arrival()
        self.__generate_meat_consumption()

    def __generate_egs_arrival(self):

        transaction = StorageTransaction()
        transaction.nomenclature = self.__nomenclature_generator.egs
        transaction.measurement_unit = self.__measurement_unit_generator.thing
        transaction.count = 12
        transaction.type = StorageTransactionType.Arrival
        transaction.storage = self.__storage_generator.main_storage
        transaction.date_time = datetime(2024, 10, 24, 15, 30, 0)

        self.__egs_arrival = transaction

    def __generate_egs_consumption(self):

        transaction = StorageTransaction()
        transaction.nomenclature = self.__nomenclature_generator.egs
        transaction.measurement_unit = self.__measurement_unit_generator.thing
        transaction.count = 10
        transaction.type = StorageTransactionType.Consumption
        transaction.storage = self.__storage_generator.main_storage
        transaction.date_time = datetime(2024, 10, 24, 16, 30, 0)

        self.__egs_consumption = transaction

    def __generate_milk_arrival(self):

        transaction = StorageTransaction()
        transaction.nomenclature = self.__nomenclature_generator.milk
        transaction.measurement_unit = self.__measurement_unit_generator.milliliter
        transaction.count = 10000
        transaction.type = StorageTransactionType.Arrival
        transaction.storage = self.__storage_generator.secondary_storage
        transaction.date_time = datetime(2024, 10, 24, 11, 20, 0)

        self.__milk_arrival = transaction

    def __generate_milk_consumption(self):

        transaction = StorageTransaction()
        transaction.nomenclature = self.__nomenclature_generator.milk
        transaction.measurement_unit = self.__measurement_unit_generator.milliliter
        transaction.count = 5000
        transaction.type = StorageTransactionType.Consumption
        transaction.storage = self.__storage_generator.secondary_storage
        transaction.date_time = datetime(2024, 10, 24, 12, 20, 0)

        self.__milk_consumption = transaction

    def __generate_meat_arrival(self):

        transaction = StorageTransaction()
        transaction.nomenclature = self.__nomenclature_generator.meat
        transaction.measurement_unit = self.__measurement_unit_generator.kilo_gram
        transaction.count = 10
        transaction.type = StorageTransactionType.Arrival
        transaction.storage = self.__storage_generator.secondary_storage
        transaction.date_time = datetime(2024, 10, 24, 11, 20, 0)

        self.__meat_arrival = transaction

    def __generate_meat_consumption(self):

        transaction = StorageTransaction()
        transaction.nomenclature = self.__nomenclature_generator.meat
        transaction.measurement_unit = self.__measurement_unit_generator.kilo_gram
        transaction.count = 7
        transaction.type = StorageTransactionType.Consumption
        transaction.storage = self.__storage_generator.secondary_storage
        transaction.date_time = datetime(2024, 10, 24, 12, 20, 0)

        self.__meat_consumption = transaction

    @property
    def list(self):
        return [
            self.__egs_arrival,
            self.__egs_consumption,
            self.__milk_arrival,
            self.__milk_consumption,
            self.__meat_arrival,
            self.__meat_consumption
        ]

