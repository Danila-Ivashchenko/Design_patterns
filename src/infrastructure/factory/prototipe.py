from src.core.util.helper.json import JsonHelper
from src.core.util.helper.validator import Validator
from src.infrastructure.data.prototype.prototype.measurement_unit import MeasurementUnitPrototype
from src.infrastructure.data.prototype.prototype.nomenclature import NomenclaturePrototype
from src.infrastructure.data.prototype.prototype.nomenclature_group import NomenclatureGroupPrototype
from src.infrastructure.data.prototype.prototype.recipe import RecipePrototype
from src.infrastructure.data.prototype.prototype.storage import StoragePrototype
from src.infrastructure.data.prototype.prototype.storage_transaction import StorageTransactionPrototype


class PrototypeFactory:

    __name_to_type = {
            'recipe': RecipePrototype,
            'nomenclature': NomenclaturePrototype,
            'nomenclature_group': NomenclatureGroupPrototype,
            'measurement_unit': MeasurementUnitPrototype,
            'storage': StoragePrototype,
            'storage_transaction': StorageTransactionPrototype
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
