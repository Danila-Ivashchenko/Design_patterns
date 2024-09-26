from entity import MeasurementUnit
from .base import BaseGenerator

class MeasurementUnitGenerator(BaseGenerator[MeasurementUnit]):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MeasurementUnitGenerator, cls).__new__(cls)
        return cls._instance

    def __init__(self):

        self.__gram = MeasurementUnit("грамм", 1.0)
        self.__kilo_gram = MeasurementUnit("килограм", 1000.0)

        self.__thing = MeasurementUnit("штука", 1.0)
        self.__tens = MeasurementUnit("десяток", 10.0)

        self.__milliliter = MeasurementUnit("миллилитр", 1.0)
        self.__liter = MeasurementUnit("литр", 1000.0)

        self.__teaspoon = MeasurementUnit("чайная ложка", 1.0)
        self.__tablespoon = MeasurementUnit("столовая ложка", 3.0, self.__teaspoon)

    @property
    def gram(self):
        return self.__gram

    @property
    def kilo_gram(self):
        return self.__kilo_gram

    @property
    def thing(self):
        return self.__thing

    @property
    def tens(self):
        return self.__tens

    @property
    def milliliter(self):
        return self.__milliliter

    @property
    def liter(self):
        return self.__liter

    @property
    def teaspoon(self):
        return self.__teaspoon

    @property
    def tablespoon(self):
        return self.__tablespoon