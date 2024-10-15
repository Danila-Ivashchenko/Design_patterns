from src.core.domain.entity.base import BaseEntity
from src.core.domain.entity.ingredient import Ingredient
from src.core.domain.abstract.typed_list import typed_list
import datetime


class Recipe(BaseEntity):

    __ingredients: list[Ingredient]
    __steps: list[str]
    __name: str
    __time: datetime.datetime

    def __init__(self, name: str = "", ingredients: list[Ingredient] = [], steps: list[str] = [], time: datetime.datetime = datetime.datetime.now()):
        super().__init__()
        self._validator.validate_type(name, str).validate_max_or_equal_length(name, 255)
        self._validator.validate_type(ingredients, list).validate()
        self._validator.validate_type(steps, list).validate()
        self._validator.validate_type(time, datetime.datetime)

        self.__ingredients = ingredients
        self.__steps = steps
        self.__name = name
        self.__time = time

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self._validator.validate_type(value, str).validate_max_or_equal_length(value, 255).validate()
        self.__name = value

    @property
    @typed_list(Ingredient)
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        self._validator.validate_type(ingredients, list).validate()
        self.__ingredients = ingredients

    @property
    @typed_list(str)
    def steps(self):
        return self.__steps

    @steps.setter
    def steps(self, steps):
        self._validator.validate_type(steps, list).validate()
        self.__steps = steps

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value: datetime):
        self._validator.validate_type(value, datetime)

        self.__time = value

    def __repr__(self):
        result = ""

        for ingredient in self.__ingredients:
            result += f"{ingredient}\n"

        for step in self.__steps:
            result += f"{step}\n"

        return result




