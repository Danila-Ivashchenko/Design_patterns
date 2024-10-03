import datetime

from entity import Recipe, Ingredient, MeasurementValue
from .base import BaseGenerator
from .nomenclature import NomenclatureGenerator
from .measurement_unit import MeasurementUnitGenerator


class RecipeGenerator(BaseGenerator[Recipe]):

    _instance = None

    __nomenclature_generator = NomenclatureGenerator()
    __measurement_unit_generator = MeasurementUnitGenerator()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RecipeGenerator, cls).__new__(cls)
        return cls._instance

    def __init__(self):

        self.__generate__fried_eggs()
        self.__generate__pasta_with_chicken()
        self.__generate_crispy_waffles_with_cinnamon()

    def get_base_recipes(self):
        return [self.fried_eggs, self.pasta_with_chicken, self.crispy_waffles_with_cinnamon]

    def __generate__fried_eggs(self):
        ingredients = []

        ingredients.append(Ingredient(
            self.__nomenclature_generator.egs,
            MeasurementValue(3.0, self.__measurement_unit_generator.thing)))

        ingredients.append(Ingredient(
            self.__nomenclature_generator.oil,
            MeasurementValue(10.0, self.__measurement_unit_generator.milliliter)))

        ingredients.append(Ingredient(
            self.__nomenclature_generator.salt,
            MeasurementValue(5.0, self.__measurement_unit_generator.gram)))

        ingredients.append(Ingredient(
            self.__nomenclature_generator.milk,
            MeasurementValue(100.0, self.__measurement_unit_generator.milliliter)))

        steps = []

        steps.append("Яйца разбиваем в глубокую миску.")
        steps.append("Добавляем соль.")
        steps.append("Вливаем молоко.")
        steps.append("Тщательно перемешиваем.")
        steps.append("В сковороде на среднем огне разогреваем растительное масло. Выливаем яичную смесь в сковороду.")
        steps.append("Нежнейший омлет на молоке готов. Приятного аппетита!")

        self.__fried_eggs = Recipe("Жареные яйца", ingredients, steps, datetime.datetime.now())


    @property
    def fried_eggs(self):
        return self.__fried_eggs

    def __generate__pasta_with_chicken(self):

        ingredients = []

        ingredients.append(Ingredient(
            self.__nomenclature_generator.pasta,
            MeasurementValue(400.0, self.__measurement_unit_generator.gram)))

        ingredients.append(Ingredient(
            self.__nomenclature_generator.chicken_fillet,
            MeasurementValue(500.0, self.__measurement_unit_generator.gram)))

        ingredients.append(Ingredient(
            self.__nomenclature_generator.salt,
            MeasurementValue(5.0, self.__measurement_unit_generator.gram)))

        ingredients.append(Ingredient(
            self.__nomenclature_generator.sour_cream,
            MeasurementValue(250.0, self.__measurement_unit_generator.gram)))

        ingredients.append(Ingredient(
            self.__nomenclature_generator.oil,
            MeasurementValue(10.0, self.__measurement_unit_generator.milliliter)))

        steps = []

        steps.append("Варим макароны.")
        steps.append("Куриное филе вымыть и обсушить.")
        steps.append("Филе нарезать кусочками.")
        steps.append("Разогреть сковороду. Налить растительное масло. Выложить филе, жарить, помешивая, на среднем огне до готовности (около 20 минут).")
        steps.append("Посолить. Перемешать. Добавить сметану. Перемешать. Накрыть крышкой. Довести до кипения и снять с огня. Оставить под крышкой еще на 5-10 минут.")
        steps.append("Налить в кастрюлю воду, вскипятить, посолить воду. В кипящую воду опустить макаронные изделия, перемешать, налить 2 ч. ложки растительного масла. Дать вскипеть, перемешать. Варить на среднем огне до готовности, согласно инструкции (7-10 минут).")
        steps.append("Откинуть на дуршлаг готовые макароны. Дать воде стечь.")
        steps.append("Выложить пасту к курице. Хорошо перемешать пасту с куриной грудкой и можно подавать.")

        self.__pasta_with_chicken = Recipe("Паста с курицей", ingredients, steps, datetime.datetime.now())

    @property
    def pasta_with_chicken(self):
        return self.__pasta_with_chicken

    def __generate_crispy_waffles_with_cinnamon(self):

        ingredients = []

        ingredients.append(Ingredient(
            self.__nomenclature_generator.wheat_flour,
            MeasurementValue(150.0, self.__measurement_unit_generator.gram)
        ))

        ingredients.append(Ingredient(
            self.__nomenclature_generator.sugar,
            MeasurementValue(60.0, self.__measurement_unit_generator.gram)
        ))

        ingredients.append(Ingredient(
            self.__nomenclature_generator.butter,
            MeasurementValue(75.0, self.__measurement_unit_generator.gram)
        ))

        ingredients.append(Ingredient(
            self.__nomenclature_generator.egs,
            MeasurementValue(2.0, self.__measurement_unit_generator.thing)))

        ingredients.append(Ingredient(
            self.__nomenclature_generator.milk,
            MeasurementValue(100.0, self.__measurement_unit_generator.milliliter)))

        ingredients.append(Ingredient(
            self.__nomenclature_generator.cinnamon,
            MeasurementValue(1.0, self.__measurement_unit_generator.teaspoon))
        )

        steps = [
            "Подготовьте ингредиенты и растопите сливочное масло на слабом огне или в микроволновке.",
            "Взбейте яйца с сахаром до получения воздушной и однородной массы.",
            "Продолжая взбивать, медленно влейте молоко и добавьте растопленное масло.",
            "В отдельной миске соедините муку, корицу и соль. Постепенно вмешивайте сухие ингредиенты в жидкую смесь до однородности.",
            "Разогрейте вафельницу и порционно выливайте тесто (примерно по столовой ложке на одну вафлю).",
            "Выпекайте вафли до золотистого цвета, около 3-4 минут, в зависимости от мощности прибора.",
            "После выпекания вафли будут мягкими, но станут хрустящими, когда остынут."
        ]

        self.__crispy_waffles_with_cinnamon = Recipe("Хрустящие вафли с корицей", ingredients, steps, datetime.datetime.now())

    @property
    def crispy_waffles_with_cinnamon(self):
        return self.__crispy_waffles_with_cinnamon
