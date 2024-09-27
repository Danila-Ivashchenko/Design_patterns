import errors
from entity.base import BaseEntity
from enums import ReportType
from report.rft_reporter import RftDownReporter
from report.markdown_reporter import MarkDownReporter
from report.csv_report import CssvReporter
from report.xml_report import XmlReporter
from report.json_report import JsonReporter


class Settings(BaseEntity):

    __organization_name= ""
    __inn = ""
    __director_name = ""
    __bik = ""
    __ownership_type = ""
    __correspondent_account = ""
    __account = ""
    __report_type: ReportType = ReportType.JSON

    __report_map = {
        ReportType.JSON: JsonReporter,
        ReportType.XML: XmlReporter,
        ReportType.CSV: CssvReporter,
        ReportType.MARKDOWN: MarkDownReporter,
        ReportType.RTF: RftDownReporter
    }

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
    def report_type(self):
        return self.__report_type

    @property
    def report_map(self):
        return self.__report_map

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


