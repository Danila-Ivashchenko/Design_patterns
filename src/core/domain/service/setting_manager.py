import json
import os
from src.core.domain.entity.settings import Settings
import src.core.domain.errors as errors
import src.core.util.helper.json as json_helper
from src.core.domain.enums.event_type import EventType
from src.core.domain.service.base.base import BaseService
from src.core.domain.service.dto.update_date_block_dto import UpdateDateBlockDTO
from src.core.util.helper.validator import Validator
from src.core.domain.enums.report_type import ReportType
from src.core.util.observer.event import Event


class SettingsManager(BaseService):
    __file_name = os.path.join("json", "settings.json")
    __json_helper = json_helper.JsonHelper()
    __settings: Settings = Settings()

    # to provide singleton
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(SettingsManager, cls).__new__(cls)

        return cls.__instance

    def __init__(self):
        super().__init__()

    def update_date_block(self, dto: UpdateDateBlockDTO):
        self._validator.validate_type(dto, UpdateDateBlockDTO).validate()

        self.__settings.date_block = dto.value

    def save(self, filename: str = "") -> bool:
        self._validator.validate_type(filename, str).validate()

        if filename == "":
            filename = self.__file_name

        try:
            full_name = f"{os.curdir}{os.sep}{filename}"
            with open(full_name, "w") as file:
                json_data = self.__json_helper.to_serialize(self.__settings)
                json.dump(json_data, file)
            return True
        except Exception as e:
            exception = errors.OperationException.fail_to_parce_json(e)
            self.__error = exception
            return False

    def open(self, filename: str = "") -> bool:
        self._validator.validate_type(filename, str).validate()

        if filename == "":
            filename = self.__file_name

        try:
            full_name = f"{os.curdir}{os.sep}{filename}"
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

    def handle_event(self, event: Event):
        super().handle_event(event)

        pass




