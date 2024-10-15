import json
import os
from src.core.domain.entity.settings import Settings
import src.core.domain.errors as errors
import src.core.util.helper.json as json_helper
from src.core.util.helper.validator import Validator
from src.core.domain.enums.report_type import ReportType


class SettingsManager:
    __file_name = os.path.join("json", "settings.json")
    __json_helper = json_helper.JsonHelper()
    __settings: Settings = Settings()
    __error: errors.AbstractException = None
    __validator: Validator = Validator()

    # to provide singleton
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(SettingsManager, cls).__new__(cls)

        return cls.__instance

    def open(self, filename: str = ""):
        self.__validator.validate_type(filename, str).validate_min_length(filename, 0).validate()

        try:
            full_name = f"{os.curdir}{os.sep}{self.__file_name}"
            with open(full_name, "r") as file:
                data = json.load(file)

                self.__convert(data)
            return True
        except Exception as e:
            exception = errors.OperationException.fail_to_parce_json(e)
            self.__error = exception
            self.__settings = self.__default_setting()

            return False

    def __convert(self, data):
        fields = self.__json_helper.parse_fields(Settings)

        data_keys = data.keys()

        for field in fields:
            if field in data_keys:
                setattr(self.__settings, field, data[field])

    @property
    def settings(self):
        return self.__settings

    @property
    def error(self):
        return self.__error

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
        data.report_default = 1

        reports_map = [
            {
              "report_type": 1,
              "handler": "CsvReporter"
            },
            {
              "report_type": 2,
              "handler": "MarkDownReporter"
            },
            {
              "report_type": 3,
              "handler": "JsonReporter"
            },
            {
              "report_type": 4,
              "handler": "XmlReporter"
            },
            {
              "report_type": 5,
              "handler": "RftDownReporter"
            }
          ]

        data.reports_map = reports_map

        return data





