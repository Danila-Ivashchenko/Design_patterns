from datetime import datetime

from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.osv import Osv
from src.core.domain.entity.storage import Storage
from src.core.domain.entity.storage_turnover import StorageTurnover
from src.core.util.helper.validator import Validator


class CreateOsvFactoryDTO:
    turnovers_to_start: list[StorageTurnover]
    turnovers_to_end: list[StorageTurnover]

    start_date: datetime
    end_date: datetime

    nomenclatures: list[Nomenclature]
    storages: list[Storage]


class OsvIndex:
    nomenclature_id: str
    storage_id: str

    def idx(self):
        return f'{self.nomenclature_id}-{self.storage_id}'


class OsvFactory:

    _validator: Validator

    def __init__(self):
        self._validator = Validator()

    def from_storage_turnovers(self, dto: CreateOsvFactoryDTO) -> list[Osv]:
        self._validator.validate_list_type(dto.turnovers_to_start, StorageTurnover).validate()
        self._validator.validate_list_type(dto.turnovers_to_end, StorageTurnover).validate()
        self._validator.validate_list_type(dto.nomenclatures, Nomenclature).validate()
        self._validator.validate_list_type(dto.storages, Storage).validate()

        result: list[Osv] = []

        turnovers_to_start_date: dict[str, list[StorageTurnover]] = dict[str, list[StorageTurnover]]()

        for turnover in dto.turnovers_to_start:
            key = OsvIndex()
            key.nomenclature_id = turnover.nomenclature.id
            key.storage_id = turnover.storage.id

            if key.idx() in turnovers_to_start_date:
                turnovers_to_start_date[key.idx()].append(turnover)
            else:
                turnovers_to_start_date[key.idx()] = [turnover]

        turnovers_to_end_date: dict[str, list[StorageTurnover]] = dict[str, list[StorageTurnover]]()

        for turnover in dto.turnovers_to_end:
            key = OsvIndex()
            key.nomenclature_id = turnover.nomenclature.id
            key.storage_id = turnover.storage.id

            if key.idx() in turnovers_to_end_date:
                turnovers_to_end_date[key.idx()].append(turnover)
            else:
                turnovers_to_end_date[key.idx()] = [turnover]

        for nomenclature in dto.nomenclatures:
            for storage in dto.storages:
                key = OsvIndex()
                key.nomenclature_id = nomenclature.id
                key.storage_id = storage.id

                start_turnovers = []
                end_turnovers = []

                if key.idx() in turnovers_to_start_date:
                    start_turnovers = turnovers_to_start_date[key.idx()]

                if key.idx() in turnovers_to_end_date:
                    end_turnovers = turnovers_to_end_date[key.idx()]

                osv = Osv()
                osv.nomenclature = nomenclature
                osv.storage = storage
                osv.start_date = dto.start_date
                osv.end_date = dto.end_date

                osv.amount_at_start = sum([turnover.amount for turnover in start_turnovers])
                osv.amount_at_end = sum([turnover.amount for turnover in end_turnovers])

                result.append(osv)

        return result
