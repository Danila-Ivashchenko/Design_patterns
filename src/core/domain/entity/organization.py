from src.core.domain.entity.base import BaseEntity
from src.core.domain.entity.settings import Settings

class Organization(BaseEntity):
    __inn = ""
    __bik = ""
    __account = ""
    __ownership_type = ""

    def __int__(self, settings: Settings):
        super().__init__()

        self.inn = settings.inn
        self.bik = settings.bik
        self.account = settings.account
        self.ownership_type = settings.ownership_type

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        self._validator.validate_type(value, str).validate_length(value, 12).validate()

        self.__inn = value

    @property
    def bik(self):
        return self.__bik

    @bik.setter
    def bik(self, value: str):
        self._validator.validate_type(value, str).validate_length(value, 9).validate()

        self.__bik = value

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value: str):
        self._validator.validate_type(value, str).validate_length(value, 11).validate()

        self.__account = value

    @property
    def ownership_type(self):
        return self.__ownership_type

    @ownership_type.setter
    def ownership_type(self, value: str):
        self._validator.validate_type(value, str).validate_length(value, 5).validate()

        self.__ownership_type = value

