from .base import BaseGenerator
from entity import Nomenclature
from .nomenclature_group import NomenclatureGroupGenerator
from .measurement_unit import MeasurementUnitGenerator


class NomenclatureGenerator(BaseGenerator[Nomenclature]):

    __nomenclature_group_generator = NomenclatureGroupGenerator()
    __measurement_unit_generator = MeasurementUnitGenerator()

    def __init__(self, ):
        food_group = self.__nomenclature_group_generator.food

        self.__egs = Nomenclature("яйца", food_group.id, self.__measurement_unit_generator.thing)
        self.__oil = Nomenclature("масло", food_group.id, self.__measurement_unit_generator.milliliter)
        self.__salt = Nomenclature("соль", food_group.id, self.__measurement_unit_generator.gram)
        self.__milk = Nomenclature("молоко", food_group.id, self.__measurement_unit_generator.milliliter)

        self.__chicken_fillet = Nomenclature("куриное филе", food_group.id, self.__measurement_unit_generator.gram)
        self.__sour_cream = Nomenclature("сметана", food_group.id, self.__measurement_unit_generator.gram)
        self.__pasta = Nomenclature("макароны", food_group.id, self.__measurement_unit_generator.gram)

        self.__wheat_flour = Nomenclature("пшеничная  мука", food_group.id, self.__measurement_unit_generator.gram)
        self.__sugar = Nomenclature("сахар", food_group.id, self.__measurement_unit_generator.gram)
        self.__butter = Nomenclature("масло", food_group.id, self.__measurement_unit_generator.gram)
        self.__cinnamon = Nomenclature("корица", food_group.id, self.__measurement_unit_generator.teaspoon)


    @property
    def egs(self):
        return self.__egs

    @property
    def oil(self):
        return self.__oil

    @property
    def salt(self):
        return self.__salt

    @property
    def milk(self):
        return self.__milk

    @property
    def chicken_fillet(self):
        return self.__chicken_fillet

    @property
    def sour_cream(self):
        return self.__sour_cream

    @property
    def pasta(self):
        return self.__pasta

    @property
    def wheat_flour(self):
        return self.__wheat_flour

    @property
    def sugar(self):
        return self.__sugar

    @property
    def butter(self):
        return self.__butter

    @property
    def cinnamon(self):
        return self.__cinnamon
