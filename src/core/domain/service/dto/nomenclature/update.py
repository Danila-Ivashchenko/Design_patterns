from src.core.domain.service.dto.base_dto import BaseDTO


class UpdateNomenclatureDTO(BaseDTO):
    __name: str = None
    __id: str
    __nomenclature_group_id: str = None
    __measurement_unit_id: str = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self._validator.validate_type(value, str).validate_max_or_equal_length(value, 255).validate()

        self.__name = value

    @property
    def nomenclature_group_id(self):
        return self.__nomenclature_group_id

    @nomenclature_group_id.setter
    def nomenclature_group_id(self, value: str):
        self._validator.validate_type(value, str).validate()

        self.__nomenclature_group_id = value

    @property
    def measurement_unit_id(self):
        return self.__measurement_unit_id

    @measurement_unit_id.setter
    def measurement_unit_id(self, value: str):
        self._validator.validate_type(value, str).validate()

        self.__measurement_unit_id = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: str):
        self._validator.validate_type(value, str).validate()

        self.__id = value
