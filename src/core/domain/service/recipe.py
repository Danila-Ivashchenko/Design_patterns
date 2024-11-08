from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.recipe import Recipe
from src.core.domain.enums.event_type import EventType
from src.core.domain.errors.not_found import NotFoundException
from src.core.domain.repository.data.data_repository import DataRepository
from src.core.domain.repository.recipe.repository import RecipeRepository
from src.core.domain.service.base.base import BaseService
from src.core.domain.service.filter import FilterService
from src.core.util.observer.event import Event


class RecipeService(BaseService):
    __filter_service: FilterService
    __nomenclature_repository: RecipeRepository
    __data_repository: DataRepository

    # to provide singleton
    __instance = None

    def __new__(cls, filter_service: FilterService):
        if cls.__instance is None:
            cls.__instance = super(RecipeService, cls).__new__(cls)

        return cls.__instance

    def __init__(self, filter_service: FilterService):
        super().__init__()

        self.__filter_service = filter_service
        self.__nomenclature_repository = RecipeRepository()
        self.__data_repository = DataRepository()

    def get_all(self) -> list[Recipe]:
        return self.__nomenclature_repository.find_all()

    def get_by_id(self, id: str) -> Recipe | None:
        return self.__nomenclature_repository.find_by_id(id)

    def delete(self, id: str):
        self._validator.validate_type(id, str).validate()

        found = self.__nomenclature_repository.find_by_id(id)

        if found is None:
            raise NotFoundException.not_found_entity_by_id("recipe", id)

        self.__nomenclature_repository.delete(id)

    def create(self, data: Recipe):
        return self.__nomenclature_repository.create(data)

    def create_multiple(self, data: list[Recipe]):
        return self.__nomenclature_repository.create_multiple(data)

    def update_nomenclature_to_recipe(self, new_nomenclature: Nomenclature):
        all_recipes = self.__nomenclature_repository.find_all()

        for recipe in all_recipes:
            for i, ingredient in enumerate(recipe.ingredients):
                if ingredient.nomenclature.id == new_nomenclature.id:
                    recipe.ingredients[i].nomenclature = new_nomenclature
                    self.__nomenclature_repository.update(recipe)

    def handle_event(self, event: Event):
        if event.type == EventType.CHANGE_NOMENCLATURE:
            self.update_nomenclature_to_recipe(event.payload)