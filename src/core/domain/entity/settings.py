import src.core.domain.errors
from src.core.domain.entity.base import BaseEntity
from src.core.domain.enums.report_type import ReportType
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


class Settings(BaseEntity):

    __organization_name= ""
    __inn = ""
    __director_name = ""
    __bik = ""
    __ownership_type = ""
    __correspondent_account = ""
    __account = ""
    __report_default: ReportType

    __reports_map = {}

    # __report_map = {
    #     ReportType.JSON: JsonReporter,
    #     ReportType.XML: XmlReporter,
    #     ReportType.CSV: CssvReporter,
    #     ReportType.MARKDOWN: MarkDownReporter,
    #     ReportType.RTF: RftDownReporter
    # }

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


