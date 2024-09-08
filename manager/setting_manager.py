import json
import os
from entity.settings import Settings
import errors
import helper.json


class SettingsManager:
    __file_name = "/json/settings.json"
    __settings: Settings = Settings()
    # to provide singleton
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(SettingsManager, cls).__new__(cls)

        return cls.__instance

    def open(self, filename: str = ""):
        if not isinstance(filename, str):
            raise errors.type.invalid_type(type(filename), str)

        if filename != "":
            self.__file_name = filename

        full_name = f"{os.curdir}{os.sep}{self.__file_name}"

        try:
            with open(full_name, "r") as file:
                data = json.load(file)

                self.__convert(data)
            return True
        except Exception as e:
            print(e) # to debug
            self.__settings = self.__default_setting()

            return False

    def __convert(self, data):
        self.__settings = helper.json.from_json(data, self.__settings)

    @property
    def settings(self):
        return self.__settings

    @staticmethod
    def __default_setting():
        data = Settings()
        data.inn = "380080920202"
        data.account = "40702810203"
        data.correspondent_account = "40702810204"
        data.bik = "044030001"
        data.organization_name = "Рога и копыта (default)"
        data.ownership_type = "общая"
        data.director_name = "Директор (default)"

        return data





