from src.core.domain.abstract.typed_list import TypedList
from src.core.util.helper.json import JsonHelper
from src.core.util.helper.validator import Validator
from src.infrastructure.data.prototype.filter.entry.filter_entry import FilterEntry
from src.infrastructure.data.prototype.filter.filter.measurement_unit import MeasurementUnitFilter
from src.infrastructure.data.prototype.filter.filter.nomenclature import NomenclatureFilter
from src.infrastructure.data.prototype.filter.filter.nomenclature_group import NomenclatureGroupFilter
from src.infrastructure.data.prototype.filter.filter.recipe import RecipeFilter


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

    def create_filter(self, entity_name: str, data: list) -> list[FilterEntry]:
        self.__validator.validate_type(entity_name, str).validate_type(data, list).validate()

        return self.__json_helper.to_deserialize(TypedList(FilterEntry), data)
        #
        # if entity_name in self.__name_to_type.keys():
        #     filter_type = self.__name_to_type[entity_name]
        #     return self.__json_helper.to_deserialize(filter_type, data)
        #
        # return None
