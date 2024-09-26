from entity import Recipe
from .interface import IRecipeRepository
from repository.base import BaseRepository
from storage import RecipeStorage


class RecipeRepository(IRecipeRepository, BaseRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(RecipeRepository, cls).__new__(cls)

        return cls.__instance

    def __init__(self):
        super().__init__()
        self.__storage = RecipeStorage()

    def create(self, data: Recipe):
        self._validator.validate_type(data, Recipe).validate()

        self.__storage.set(data.id, data)

    def create_multiple(self, data: list[Recipe]):
        self._validator.validate_list_type(data, Recipe).validate()

        data_to_save = {}

        for recipe in data:
            data_to_save[recipe.id] = recipe

        self.__storage.set_multiple(data_to_save)

    def update(self, data: Recipe):
        self._validator.validate_type(data, Recipe).validate()

        self.__storage.set(data.id, data)

    def update_multiple(self, data: list[Recipe]):
        self._validator.validate_type(data, list[Recipe]).validate()

        data_to_save = {}

        for recipe in data:
            data_to_save[recipe.id] = recipe

        self.__storage.set_multiple(data_to_save)

    def find_by_id(self, id: str) -> Recipe:
        self._validator.validate_type(id, str).validate()

        return self.__storage.get(id)

    def find_all(self) -> list[Recipe]:
        return self.__storage.get_all()

    def delete(self, id: str):
        self._validator.validate_type(id, str).validate()

        self.__storage.remove(id)

    def delete_multiple(self, ids: list[str]):
        self._validator.validate_type(ids, list[str]).validate()

