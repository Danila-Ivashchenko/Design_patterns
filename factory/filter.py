from prototype import NomenclatureFilter, NomenclatureGroupFilter, MeasurementUnitFilter, RecipeFilter
from helper import JsonHelper
from helper.validator import Validator


class FilterFactory:

    __name_to_type = {
            'recipe': RecipeFilter,
            'nomenclature': NomenclatureFilter,
            'nomenclature_group': NomenclatureGroupFilter,
            'measurement_unit': MeasurementUnitFilter
    }

    __json_helper: JsonHelper
    __validator: Validator

    def __init__(self):

        self.__json_helper = JsonHelper()
        self.__validator = Validator()

    def create_filter(self, entity_name: str, data: dict):
        self.__validator.validate_type(entity_name, str).validate_type(data, dict).validate()

        if entity_name in self.__name_to_type.keys():
            filter_type = self.__name_to_type[entity_name]
            return self.__json_helper.to_deserialize(filter_type, data)

        return None
