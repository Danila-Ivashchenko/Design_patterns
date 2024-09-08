import errors

class Settings:

    __organization_name= ""
    __inn = ""
    __director_name = ""
    __bik = ""
    __ownership_type = ""
    __correspondent_account = ""
    __account = ""

    @property
    def organization_name(self):
        return self.__organization_name

    @organization_name.setter
    def organization_name(self, value: str):
        if not isinstance(value, str):
            raise errors.type.invalid_type(type(value), str)

        self.__organization_name = value

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value):
        if not isinstance(value, str):
            raise errors.type.invalid_type(type(value), str)

        if len(value) != 12:
            raise errors.value.invalid_length(len(value), 12)

        self.__inn = value

    @property
    def director_name(self):
        return self.__director_name

    @director_name.setter
    def director_name(self, value):
        if not isinstance(value, str):
            raise errors.type.invalid_type(type(value), str)

        self.__director_name = value

    @property
    def bik(self):
        return self.__bik

    @bik.setter
    def bik(self, value):
        if not isinstance(value, str):
            raise errors.type.invalid_type(type(value), str)

        if len(value) != 9:
            raise errors.value.invalid_length(len(value), 9)

        self.__bik = value

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value):
        if not isinstance(value, str):
            raise errors.type.invalid_type(type(value), str)

        if len(value) != 11:
            raise errors.value.invalid_length(len(value), 11)

        self.__account = value

    @property
    def correspondent_account(self):
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value):
        if not isinstance(value, str):
            raise errors.type.invalid_type(type(value), str)

        if len(value) != 11:
            raise errors.value.invalid_length(len(value), 11)

        self.__correspondent_account = value

    @property
    def ownership_type(self):
        return self.__ownership_type

    @ownership_type.setter
    def ownership_type(self, value):
        if not isinstance(value, str):
            raise errors.type.invalid_type(type(value), str)

        if len(value) != 5:
            raise errors.value.invalid_length(len(value), 5)

        self.__ownership_type = value

    def validate(self):
        if self.inn == "":
            raise errors.value.value_does_not_set("inn")

        if self.account == "":
            raise errors.value.value_does_not_set("account")

        if self.correspondent_account == "":
            raise errors.value.value_does_not_set("correspondent_account")

        if self.bik == "":
            raise errors.value.value_does_not_set("bik")

        if self.organization_name == "":
            raise errors.value.value_does_not_set("organization_name")

        if self.ownership_type == "":
            raise errors.value.value_does_not_set("ownership_type")

        if self.director_name == "":
            raise errors.value.value_does_not_set("director_name")

    def __repr__(self):
        res = ""
        res += f"inn: {self.inn}\n"
        res += f"account: {self.account}\n"
        res += f"correspondent_account: {self.correspondent_account}\n"
        res += f"bik: {self.bik}\n"
        res += f"organization_name: {self.organization_name}\n"
        res += f"ownership_type: {self.ownership_type}\n"
        res += f"director_name: {self.director_name}\n"

        return res


