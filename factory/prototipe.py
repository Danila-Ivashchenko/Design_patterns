from prototype import NomenclaturePrototype, NomenclatureGroupPrototype, RecipePrototype, MeasurementUnitPrototype, BasePrototype
from helper import JsonHelper
from helper.validator import Validator


class PrototypeFactory:

    __name_to_type = {
            'recipe': RecipePrototype,
            'nomenclature': NomenclaturePrototype,
            'nomenclature_group': NomenclatureGroupPrototype,
            'measurement_unit': MeasurementUnitPrototype
    }

    __json_helper: JsonHelper
    __validator: Validator

    def __init__(self):

        self.__json_helper = JsonHelper()
        self.__validator = Validator()

    def create_prototype(self, entity_name, data):
        self.__validator.validate_type(entity_name, str).validate_type(data, list).validate()

        if entity_name in self.__name_to_type.keys():
            prototype_type = self.__name_to_type[entity_name]
            return prototype_type(data)

        return None
