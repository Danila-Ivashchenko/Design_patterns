from errors.abstract import AbstractException
from service.base import BaseService
from repository.recipe import IRecipeRepository
from generator import RecipeGenerator
from entity import Recipe


class StartService(BaseService):

    __recipe_repository: IRecipeRepository

    def __init__(self, recipe_repo: IRecipeRepository):
        super().__init__()

        self._validator.validate_type(recipe_repo, IRecipeRepository).validate()

        self.__recipe_repository = recipe_repo
        self.__start()

    def __start(self):
        recipe_generator = RecipeGenerator()

        recipes = recipe_generator.get_base_recipes()

        try:
            self.__recipe_repository.create_multiple(recipes)
        except AbstractException as e:
            self.__error = e

    @property
    def get_all_recipes(self):
        try:
            return self.__recipe_repository.find_all()
        except AbstractException as e:
            self.__error = e

    def create_recipe(self, data: Recipe):
        try:
            self.__recipe_repository.create(data)
        except AbstractException as e:
            self.__error = e

    def get_by_id(self, id: str):
        try:
            return self.__recipe_repository.find_by_id(id)
        except AbstractException as e:
            self.__error = e