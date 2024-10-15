from  src.infrastructure.data.generator.base import BaseGenerator
from src.core.domain.entity.nomenclature_group import NomenclatureGroup



class NomenclatureGroupGenerator(BaseGenerator[NomenclatureGroup]):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NomenclatureGroupGenerator, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.__food = NomenclatureGroup("еда")

    @property
    def food(self):
        return self.__food

    @property
    def list(self):
        return [self.food]
