from datetime import datetime

from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.storage_transaction import StorageTransaction
from src.core.domain.entity.storage_turnover import StorageTurnover
from src.core.util.helper.validator import Validator


class TurnoverIndex:
    nomenclature_id: str
    storage_id: str
    measurement_unit_id: str

    def idx(self):
        return f'{self.nomenclature_id}-{self.storage_id}-{self.measurement_unit_id}'

class StorageTurnoverFactory:

    _validator: Validator

    def __init__(self):
        self._validator = Validator()

    def create_turnovers(self, data: list[StorageTransaction], start_date: datetime, end_date: datetime) -> list[StorageTurnover]:
        self._validator.validate_list_type(data, StorageTransaction).validate()
        transactions_map = {}

        for transaction in data:
            key = TurnoverIndex()
            key.nomenclature_id = transaction.nomenclature.id
            key.storage_id = transaction.storage.id
            key.measurement_unit_id = transaction.measurement_unit.id

            if key.idx() not in transactions_map:
                transactions_map[key.idx()] = []

            transactions_map[key.idx()].append(transaction)

        result = []

        for key in transactions_map:
            result.append(self.create(transactions_map[key]))

        return result

    def create(self, transactions: list[StorageTransaction]) -> StorageTurnover:
        storage_turnover = StorageTurnover()
        storage_turnover.amount = float(0)

        nomenclature = None
        measurement_unit = None
        storage = None

        for transaction in transactions:
            if nomenclature is None:
                nomenclature = transaction.nomenclature
                storage = transaction.storage
            else:
                if nomenclature.id != transaction.nomenclature.id:
                    raise Exception("Transactions must be from the same nomenclature")
            if measurement_unit is None:
                measurement_unit = transaction.measurement_unit
            else:
                if measurement_unit.id != transaction.measurement_unit.id:
                    raise Exception("Transactions must be from the same measurement unit")

            if storage is None:
                storage = transaction.storage
            else:
                if storage.id != transaction.storage.id:
                    raise Exception("Transactions must be from the same storage")

            storage_turnover.amount += transaction.amount

        if nomenclature is not None:
            storage_turnover.nomenclature = nomenclature
        if storage is not None:
            storage_turnover.storage = storage
        if measurement_unit is not None:
            storage_turnover.measurement_unit = measurement_unit

        return storage_turnover
