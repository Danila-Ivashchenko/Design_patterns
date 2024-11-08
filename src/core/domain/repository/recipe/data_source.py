from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.entity.recipe import Recipe
from src.core.domain.entity.storage_turnover import StorageTurnover
from src.core.util.helper.validator import Validator


class RecipeDataSource:

    __validator: Validator
    __data = {}
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(RecipeDataSource, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__validator = Validator()

    def create(self, recipe: Recipe) -> Recipe:
        self.__validator.validate_type(recipe, Recipe).validate()

        self.__data[recipe.id] = recipe

        return recipe

    def get_all(self) -> list[Recipe]:
        return list(self.__data.values())

    def get_by_id(self, id: str) -> Recipe | None:
        self.__validator.validate_type(id, str).validate()

        result = None

        if id in self.__data:
            result = self.__data[id]

        return result

    def create_multiple(self, recipes: list[Recipe]) -> list[Recipe]:
        self.__validator.validate_list_type(recipes, Recipe).validate()

        result = []

        for recipe in recipes:
            result.append(self.create(recipe))

        return result

    def delete(self, id: str):
        self.__validator.validate_type(id, str).validate()

        if id in self.__data:
            del self.__data[id]
