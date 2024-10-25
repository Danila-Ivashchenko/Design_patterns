from src.core.domain.entity.base import BaseEntity


class Storage(BaseEntity):
    __name: str
    __location: str

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self._validator.validate_type(value, str).validate()

        self.__name = value

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, value: str):
        self._validator.validate_type(value, str).validate()

        self.__location = value
    