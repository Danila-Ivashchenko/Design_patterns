from datetime import datetime

import src.core.domain.errors
from src.core.domain.entity.base import BaseEntity
from src.core.domain.enums.report_type import ReportType
from src.core.util.logger.entry import LogLevel
from src.infrastructure.report.rft_reporter import RftDownReporter
from src.infrastructure.report.markdown_reporter import MarkDownReporter
from src.infrastructure.report.csv_report import CsvReporter
from src.infrastructure.report.xml_report import XmlReporter
from src.infrastructure.report.json_report import JsonReporter


class ReportHandler(BaseEntity):
    __type: ReportType
    __handler: str

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, value: int):
        self._validator.validate_type(value, int)

        self.__type = ReportType(int)

    @property
    def handler(self):
        return self.__handler

    @handler.setter
    def handler(self, value: str):
        self._validator.validate_type(value, str)

        self.__handler = value

    def __dict__(self):
        return {
            'type': self.type.name,
            'handler': self.handler
        }


class Settings(BaseEntity):

    __organization_name: str = ""
    __inn: str = ""
    __director_name: str = ""
    __bik: str = ""
    __ownership_type: str = ""
    __correspondent_account: str = ""
    __account: str = ""
    __date_block: datetime = datetime.min
    __report_default: ReportType
    __first_start = True
    __data_path = ""
    __log_level = LogLevel.DEBUG
    __log_file = ""

    __reports_map = {}

    def __init__(self):
        super().__init__()
    @property
    def organization_name(self):
        return self.__organization_name

    @organization_name.setter
    def organization_name(self, value: str):
        self._validator.validate_type(value, str).validate()

        self.__organization_name = value

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        self._validator.validate_type(value, str).validate_length(value, 12).validate()

        self.__inn = value

    @property
    def director_name(self):
        return self.__director_name

    @director_name.setter
    def director_name(self, value):
        self._validator.validate_type(value, str).validate()

        self.__director_name = value

    @property
    def bik(self):
        return self.__bik

    @bik.setter
    def bik(self, value):
        self._validator.validate_type(value, str).validate_length(value, 9).validate()

        self.__bik = value

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value):
        self._validator.validate_type(value, str).validate_length(value, 11).validate()

        self.__account = value

    @property
    def correspondent_account(self):
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value):
        self._validator.validate_type(value, str).validate_length(value, 11).validate()

        self.__correspondent_account = value

    @property
    def ownership_type(self):
        return self.__ownership_type

    @ownership_type.setter
    def ownership_type(self, value):
        self._validator.validate_type(value, str).validate_length(value, 5).validate()

        self.__ownership_type = value

    @property
    def report_default(self):
        return self.__report_default

    @report_default.setter
    def report_default(self, value: int):
        self._validator.validate_type(value, int)

        self.__report_default = ReportType(value)

    @property
    def reports_map(self):
        return self.__reports_map

    @reports_map.setter
    def reports_map(self, value: list):
        self._validator.validate_type(value, list).validate()

        for item in value:
            handler = ReportHandler

            handler.type = ReportType(item["report_type"])
            handler.handler = item["handler"]

            self.__reports_map[handler.type] = eval(handler.handler)

    @property
    def date_block(self):
        return self.__date_block

    @date_block.setter
    def date_block(self, value: datetime|int):
        self._validator.validate_on_of_type(value, (datetime, int)).validate()
        if isinstance(value, int):
            value = datetime.fromtimestamp(value)

        self.__date_block = value

    @property
    def first_start(self):
        return self.__first_start

    @first_start.setter
    def first_start(self, value: bool):
        self._validator.validate_type(value, bool)

        self.__first_start = value

    @property
    def data_path(self):
        return self.__data_path

    @data_path.setter
    def data_path(self, value: str):
        self._validator.validate_type(value, str)

        self.__data_path = value

    @property
    def log_level(self):
        return self.__log_level

    @log_level.setter
    def log_level(self, value: int):
        self._validator.validate_type(value, int)

        self.__log_level = LogLevel(value)

    @property
    def log_file(self):
        return self.__log_file

    @log_file.setter
    def log_file(self, value: str):
        self._validator.validate_type(value, str)

        self.__log_file = value

    def to_dict(self):
        result = {
            "inn": self.inn,
            "account": self.account,
            "correspondent_account": self.correspondent_account,
            "bik": self.bik,
            "organization_name": self.organization_name,
            "ownership_type": self.ownership_type,
            "director_name": self.director_name,
            "report_default": self.report_default.value,
            "date_block": int(self.date_block.timestamp()),
            "first_start": self.first_start,
            "data_path": self.data_path,
            "log_level": self.log_level.value,
            "log_file": self.log_file
        }

        reports = []

        for key, value in self.reports_map.items():
            reports.append({
                "report_type": key.value,
                "handler": value.class_name()
            })

        result["reports_map"] = reports

        return result

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


