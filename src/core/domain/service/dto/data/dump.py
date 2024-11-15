from src.core.domain.service.dto.base_dto import BaseDTO


class DumpDTO(BaseDTO):
    __filename: str = ""

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, value: str):
        self._validator.validate_type(value, str).validate()

        self.__filename = value