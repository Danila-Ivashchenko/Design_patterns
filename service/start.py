from errors.abstract import AbstractException
from service.base import BaseService
from repository.recipe import IRecipeRepository
from repository.data import DataRepository
from generator import RecipeGenerator, NomenclatureGenerator, NomenclatureGroupGenerator, MeasurementUnitGenerator
from factory import FilterFactory, PrototypeFactory
from prototype import NomenclaturePrototype
from entity import Recipe


class StartService(BaseService):

    __data_repository: DataRepository
    __filter_factory: FilterFactory
    __prototype_factory: PrototypeFactory

    def __init__(self, data_repo: DataRepository):
        super().__init__()

        self._validator.validate_type(data_repo, DataRepository).validate()

        self.__data_repository = data_repo
        self.__prototype_factory = PrototypeFactory()
        self.__filter_factory = FilterFactory()
        self.__start()

    def __start(self):
        recipe_generator = RecipeGenerator()
        nomenclature_generator = NomenclatureGenerator()
        nomenclature_group_generator = NomenclatureGroupGenerator()
        measurement_unit_generator = MeasurementUnitGenerator()

        recipes = recipe_generator.get_base_recipes()
        nomenclature = nomenclature_generator.list
        nomenclature_groups = nomenclature_group_generator.list
        measurement_units = measurement_unit_generator.list

        self.__data_repository.data[DataRepository.nomenclature_group_key()] = nomenclature_groups
        self.__data_repository.data[DataRepository.nomenclature_key()] = nomenclature
        self.__data_repository.data[DataRepository.measurement_unit_key()] = measurement_units
        self.__data_repository.data[DataRepository.receipt_key()] = recipes

    def get_by_unit_name(self, entity_name):
        self._validator.validate_type(entity_name, str)
        self._validator.validate_value_exists(entity_name, self.__data_repository.get_all_keys()).validate()

        return self.__data_repository.data[entity_name]

    def get_by_entity_and_fiter_data(self, entity_name: str, data: dict):
        self._validator.validate_type(entity_name, str).validate_type(data, dict).validate()

        units = self.get_by_unit_name(entity_name)

        filter_dto = self.__filter_factory.create_filter(entity_name, data)
        prototype = self.__prototype_factory.create_prototype(entity_name, units)

        return prototype.create(filter_dto)

    @property
    def get_all_nomenclature(self):
        return self.__data_repository.data[DataRepository.nomenclature_key()]

    @property
    def get_all_recipes(self):
        return self.__data_repository.data[DataRepository.receipt_key()]

    @property
    def get_all_nomenclature_group(self):
        return self.__data_repository.data[DataRepository.nomenclature_group_key()]

    @property
    def get_all_measurement_unit(self):
        return self.__data_repository.data[DataRepository.measurement_unit_key()]