from datetime import datetime
from datetime import timedelta
import random

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
        self.__generate_a_lot_of()

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

    def __generate_a_lot_of(self):

        dates = [
            datetime(2024, 11, 1, 10, 0, 0),
            datetime(2024, 11, 2, 10, 0, 0),
            datetime(2024, 11, 3, 10, 0, 0),
            datetime(2024, 11, 4, 10, 0, 0),
            datetime(2024, 11, 5, 10, 0, 0),
        ]

        storages = [
            self.__storage_generator.main_storage,
            self.__storage_generator.secondary_storage,
        ]

        nomenclatures = [
            self.__nomenclature_generator.egs,
            self.__nomenclature_generator.milk,
            self.__nomenclature_generator.meat,
            self.__nomenclature_generator.oil,
            self.__nomenclature_generator.butter,
            self.__nomenclature_generator.salt,
            self.__nomenclature_generator.sugar,
            self.__nomenclature_generator.cinnamon,
            self.__nomenclature_generator.wheat_flour,
            self.__nomenclature_generator.chicken_fillet,
            self.__nomenclature_generator.sour_cream,
            self.__nomenclature_generator.pasta,
        ]

        transactions = []

        time_deltas = [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        ]

        for date in dates:
            for delta in time_deltas:
                date += timedelta(hours=delta)
                for storage in storages:
                    for nomenclature in nomenclatures:

                        transaction = StorageTransaction()
                        transaction.nomenclature = nomenclature
                        transaction.measurement_unit = self.__measurement_unit_generator.thing
                        transaction.count = random.randint(10, 100)

                        if random.random() > 0.5:
                            transaction.type = StorageTransactionType.Consumption
                        else:
                            transaction.type = StorageTransactionType.Arrival

                        transaction.storage = storage
                        transaction.date_time = date

                        transactions.append(transaction)

        self.__transactions = transactions

        return transactions


    @property
    def list(self):
        return self.__transactions

