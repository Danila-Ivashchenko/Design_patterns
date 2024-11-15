import json
from xml.etree.ElementTree import indent

from src.core.domain import errors
from src.core.domain.entity.nomenclature_group import NomenclatureGroup
from src.core.domain.enums.event_type import EventType
from src.core.domain.repository.data.data_repository import DataRepository
from src.core.domain.repository.measurement_unit.repository import MeasurementUnitRepository
from src.core.domain.repository.nomenclature.repository import NomenclatureRepository
from src.core.domain.repository.nomenclature_group.repository import NomenclatureGroupRepository
from src.core.domain.repository.recipe.repository import RecipeRepository
from src.core.domain.repository.storage.repository import StorageRepository
from src.core.domain.repository.storage_transaction.repository import StorageTransactionRepository
from src.core.domain.service.base.base import BaseService
from src.core.domain.service.data import DataService
from src.core.domain.service.setting_manager import SettingsManager
from src.core.util.observer.event import Event
from src.infrastructure.data.generator.measurement_unit import MeasurementUnitGenerator
from src.infrastructure.data.generator.nomenclature import NomenclatureGenerator
from src.infrastructure.data.generator.nomenclature_group import NomenclatureGroupGenerator
from src.infrastructure.data.generator.recipe import RecipeGenerator
from src.infrastructure.data.generator.storage import StorageGenerator
from src.infrastructure.data.generator.storage_transaction import StorageTransactionGenerator


class StartService(BaseService):

    __data_repository: DataRepository
    __nomenclature_repository: NomenclatureRepository
    __settings_manager: SettingsManager
    __data_service: DataService

    def __init__(self, data_repo: DataRepository):
        super().__init__()

        self._validator.validate_type(data_repo, DataRepository).validate()

        self.__data_repository = data_repo

        self.__nomenclature_repository = NomenclatureRepository()
        self.__recipe_repository = RecipeRepository()
        self.__measurement_unit_repository = MeasurementUnitRepository()
        self.__storage_transaction_repository = StorageTransactionRepository()
        self.__storage_repository = StorageRepository()
        self.__nomenclature_group_repository = NomenclatureGroupRepository()

        self.__settings_manager = SettingsManager()
        self.__data_service = DataService()

        settings = self.__settings_manager.settings

        if settings.first_start:
            self.__start()
        else:
            self.__start_from_data_path()

    def __start_from_data_path(self):
        data_path = self.__settings_manager.settings.data_path

        if data_path == "":
            raise errors.OperationException.empty_data_path()

        try:
            with open(data_path, "r", encoding="utf-8") as file:
                data = json.load(file)

                self.__data_service.save_from_json(data)
        except Exception as e:
            raise errors.OperationException.fail_to_parce_json(e)

    def save_dump(self, filename = ""):

        if filename == "":
            filename = self.__settings_manager.settings.data_path

        if filename == "":
            raise errors.OperationException.empty_data_path()

        try:
            with open(filename, "w", encoding="utf-8") as file:
                data = self.__data_service.dump_json()
                json.dump(data, file, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            exception = errors.OperationException.fail_to_parce_json(e)
            self.__error = exception
            return False

    def __start(self):
        recipe_generator = RecipeGenerator()
        nomenclature_generator = NomenclatureGenerator()
        nomenclature_group_generator = NomenclatureGroupGenerator()
        measurement_unit_generator = MeasurementUnitGenerator()
        storage_generator = StorageGenerator()
        storage_transaction_generator = StorageTransactionGenerator()

        recipes = recipe_generator.get_base_recipes()
        nomenclature = nomenclature_generator.list
        nomenclature_groups = nomenclature_group_generator.list
        measurement_units = measurement_unit_generator.list
        storages = storage_generator.list
        storage_transactions = storage_transaction_generator.list

        self.__data_repository.data[DataRepository.nomenclatura_group_key()] = nomenclature_groups
        # self.__data_repository.data[DataRepository.nomenclature_key()] = nomenclature
        self.__data_repository.data[DataRepository.measurement_unit_key()] = measurement_units
        # self.__data_repository.data[DataRepository.recipe_key()] = recipes
        self.__data_repository.data[DataRepository.storage_key()] = storages
        self.__data_repository.data[DataRepository.storage_transaction_key()] = storage_transactions

        self.__nomenclature_repository.create_multiple(nomenclature)
        self.__recipe_repository.create_multiple(recipes)
        self.__measurement_unit_repository.create_multiple(measurement_units)
        self.__storage_transaction_repository.create_multiple(storage_transactions)
        self.__storage_repository.create_multiple(storages)
        self.__nomenclature_group_repository.create_multiple(nomenclature_groups)

    def get_by_unit_name(self, entity_name):
        self._validator.validate_type(entity_name, str)
        self._validator.validate_value_exists(entity_name, self.__data_repository.get_all_keys()).validate()

        return self.__data_repository.data[entity_name]

    @property
    def get_all_nomenclature(self):
        return self.__data_repository.data[DataRepository.nomenclature_key()]

    @property
    def get_all_recipes(self):
        return self.__data_repository.data[DataRepository.recipe_key()]

    @property
    def get_all_nomenclature_group(self):
        return self.__data_repository.data[DataRepository.nomenclatura_group_key()]

    @property
    def get_all_measurement_unit(self):
        return self.__data_repository.data[DataRepository.measurement_unit_key()]

    @property
    def get_all_storage(self):
        return self.__data_repository.data[DataRepository.storage_key()]

    @property
    def get_all_storage_transaction(self):
        return self.__data_repository.data[DataRepository.storage_transaction_key()]

    def handle_event(self, event: Event):
        super().handle_event(event)

        if event.type == EventType.DUMP_DATA:
            filename = event.payload

            self.save_dump(filename)
