from src.core.domain.abstract.typed_list import TypedList
from src.core.domain.entity.measurement_unit import MeasurementUnit
from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.nomenclature_group import NomenclatureGroup
from src.core.domain.entity.recipe import Recipe
from src.core.domain.entity.storage import Storage
from src.core.domain.entity.storage_transaction import StorageTransaction
from src.core.domain.entity.storage_turnover import StorageTurnover
from src.core.domain.repository.base.base import BaseRepository
from src.core.domain.repository.data.data_repository import DataRepository
from src.core.domain.repository.measurement_unit.repository import MeasurementUnitRepository
from src.core.domain.repository.nomenclature.repository import NomenclatureRepository
from src.core.domain.repository.nomenclature_group.repository import NomenclatureGroupRepository
from src.core.domain.repository.recipe.repository import RecipeRepository
from src.core.domain.repository.storage.repository import StorageRepository
from src.core.domain.repository.storage_transaction.repository import StorageTransactionRepository
from src.core.domain.repository.storage_turnover.repository import StorageTurnoverRepository
from src.core.domain.service.base.base import BaseService
from src.core.domain.service.filter import FilterService
from src.core.domain.service.start import StartService
from src.core.util.helper.json import JsonHelper
from src.core.util.observer.event import Event

# "nomenclature": nomenclature_service,
# "recipe": recipe_service,
# "measurement_unit": measurement_unit_service


class DataService(BaseService):
    
    __data_repository: DataRepository = None

    __nomenclature_repository: NomenclatureRepository = None
    __recipe_repository: RecipeRepository = None
    __storage_turnover_repository: StorageTurnoverRepository = None
    __measurement_unit_repository: MeasurementUnitRepository
    __storage_transaction_repository: StorageTransactionRepository = None
    __storage_repository: StorageRepository = None
    __nomenclature_group_repository: NomenclatureGroupRepository = None

    __name_to_repository: dict[str: BaseRepository]

    __start_service: StartService

    __json_helper: JsonHelper

    # to provide singleton
    __instance = None

    def __new__(cls, start_service: StartService):
        if cls.__instance is None:
            cls.__instance = super(DataService, cls).__new__(cls)

        return cls.__instance

    def __init__(self, start_service: StartService):
        super().__init__()

        self.__data_repository = DataRepository()

        self.__nomenclature_repository = NomenclatureRepository()
        self.__recipe_repository = RecipeRepository()
        self.__storage_turnover_repository = StorageTurnoverRepository()
        self.__measurement_unit_repository = MeasurementUnitRepository()
        self.__storage_transaction_repository = StorageTransactionRepository()
        self.__nomenclature_group_repository = NomenclatureGroupRepository()
        self.__storage_repository = StorageRepository()

        self.__start_service = start_service

        self.__json_helper = JsonHelper()

        self.__name_to_repository = {
            "nomenclature":  self.__nomenclature_repository,
            "recipe": self.__recipe_repository,
            "measurement_unit": self.__measurement_unit_repository,
            "storage_transaction": self.__storage_transaction_repository,
            "storage_turnover": self.__storage_turnover_repository,
            "nomenclature_group": self.__nomenclature_group_repository,
            "storage": self.__storage_repository,
        }

        self.__name_to_type = {
            "nomenclature": Nomenclature,
            "recipe": Recipe,
            "measurement_unit": MeasurementUnit,
            "storage_transaction": StorageTransaction,
            "storage_turnover": StorageTurnover,
            "nomenclature_group": NomenclatureGroup,
            "storage": Storage,
        }

    def from_json(self, data: dict):
        result = {}

        for key in data.keys():
            if key in self.__name_to_type:
                entity_type = self.__name_to_type[key]

                entity_data = self.__json_helper.to_deserialize(TypedList(entity_type), data[key])

                result[key] = entity_data

        return result

    def dump_json(self):
        result = {}

        for entity_name in self.__name_to_repository.keys():
            result[entity_name] = self.__name_to_repository[entity_name].dump_json()

        return result

    def save_by_entity_name(self, entity: str, data: list):
        if entity in self.__name_to_repository.keys():
            self.__name_to_repository[entity].create_multiple(data)

    def get_by_entity_name(self, entity: str) -> list:
        self._validator.validate_type(entity, str).validate()

        result = []

        if entity in self.__name_to_repository.keys():
            result = self.__name_to_repository[entity].find_all()
        else:
            result = self.__start_service.get_by_unit_name(entity)

        return result

    def handle_event(self, event: Event):
        super().handle_event(event)