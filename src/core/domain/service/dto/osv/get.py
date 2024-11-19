from datetime import datetime

from src.core.domain.service.dto.base_dto import BaseDTO


class OsvGetDTO(BaseDTO):
    __start_date: datetime
    __end_date: datetime
    __storage_id: str = None

    @property
    def start_date(self) -> datetime:
        return self.__start_date

    @start_date.setter
    def start_date(self, value: datetime | int | float):
        if isinstance(value, (int, float)):
            value = datetime.fromtimestamp(value)

        self._validator.validate_type(value, datetime).validate()
        self.__start_date = value

    @property
    def end_date(self) -> datetime:
        return self.__end_date

    @end_date.setter
    def end_date(self, value: datetime | int | float):
        if isinstance(value, (int, float)):
            value = datetime.fromtimestamp(value)

        self._validator.validate_type(value, datetime).validate()
        self.__end_date = value

    @property
    def storage_id(self) -> str:
        return self.__storage_id

    @storage_id.setter
    def storage_id(self, value: str):
        self._validator.validate_type(value, str).validate()

        self.__storage_id = value