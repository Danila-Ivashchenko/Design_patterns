from src.core.domain.entity.storage_turnover import StorageTurnover
from src.infrastructure.data.generator.base import BaseGenerator
from src.infrastructure.data.generator.measurement_unit import MeasurementUnitGenerator
from src.infrastructure.data.generator.nomenclature import NomenclatureGenerator
from src.infrastructure.data.generator.storage import StorageGenerator


class StorageTurnoverGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

        self.__storage_generator = StorageGenerator()
        self.__nomenclature_generator = NomenclatureGenerator()
        self.__measurement_unit_generator = MeasurementUnitGenerator()

        self.__generate()

    def __generate(self):
        pass
    # def __generate_egs_turnover(self):
    #
    #     turnover = StorageTurnover()

