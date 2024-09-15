from entity.base import BaseEntity
from entity import Settings

class Organization(BaseEntity):
    __inn = ""
    __bik = ""
    __account = ""
    __ownership_type = ""

    def __int__(self, settings: Settings):
        super().__init__()

        self.__inn = settings.inn
        self.__bik = settings.bik
        self.__account = settings.account
        self.__ownership_type = settings.ownership_type

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        self.__inn = value

    @property
    def bik(self):
        return self.__bik

    @bik.setter
    def bik(self, value: str):
        self.__bik = value

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value: str):
        self.__account = value

    @property
    def ownership_type(self):
        return self.__ownership_type

    @ownership_type.setter
    def ownership_type(self, value: str):
        self.__ownership_type = value

