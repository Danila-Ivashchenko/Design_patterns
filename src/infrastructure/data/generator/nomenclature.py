from src.infrastructure.data.generator.base import BaseGenerator
from src.core.domain.entity.nomenclature import Nomenclature
from src.infrastructure.data.generator.nomenclature_group import NomenclatureGroupGenerator
from src.infrastructure.data.generator.measurement_unit import MeasurementUnitGenerator


class NomenclatureGenerator(BaseGenerator[Nomenclature]):

    __nomenclature_group_generator = NomenclatureGroupGenerator()
    __measurement_unit_generator = MeasurementUnitGenerator()

    __instance = None
    __list = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(NomenclatureGenerator, cls).__new__(cls)

        return cls.__instance

    def __init__(self):
        if len(self.list) > 0:
            return
        food_group = self.__nomenclature_group_generator.food

        self.__egs = Nomenclature("яйца", food_group.id, self.__measurement_unit_generator.thing)
        self.__oil = Nomenclature("масло растительное", food_group.id, self.__measurement_unit_generator.liter)
        self.__salt = Nomenclature("соль", food_group.id, self.__measurement_unit_generator.gram)
        self.__milk = Nomenclature("молоко", food_group.id, self.__measurement_unit_generator.milliliter)
        self.__meat = Nomenclature("мясо", food_group.id, self.__measurement_unit_generator.kilo_gram)

        self.__chicken_fillet = Nomenclature("куриное филе", food_group.id, self.__measurement_unit_generator.gram)
        self.__sour_cream = Nomenclature("сметана", food_group.id, self.__measurement_unit_generator.gram)
        self.__pasta = Nomenclature("макароны", food_group.id, self.__measurement_unit_generator.gram)

        self.__wheat_flour = Nomenclature("пшеничная  мука", food_group.id, self.__measurement_unit_generator.gram)
        self.__sugar = Nomenclature("сахар", food_group.id, self.__measurement_unit_generator.gram)
        self.__butter = Nomenclature("масло сливочное", food_group.id, self.__measurement_unit_generator.gram)
        self.__cinnamon = Nomenclature("корица", food_group.id, self.__measurement_unit_generator.teaspoon)


        self.__list.append(self.meat)
        self.__list.append(self.egs)
        self.__list.append(self.oil)
        self.__list.append(self.salt)
        self.__list.append(self.milk)

        self.__list.append(self.chicken_fillet)
        self.__list.append(self.sour_cream)
        self.__list.append(self.pasta)

        self.__list.append(self.wheat_flour)
        self.__list.append(self.sugar)
        self.__list.append(self.butter)
        self.__list.append(self.cinnamon)

    @property
    def list(self):
        return self.__list

    @property
    def meat(self):
        return self.__meat

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
