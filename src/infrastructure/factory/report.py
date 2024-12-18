from src.core.domain.entity.settings import Settings
from src.core.domain.enums.report_type import ReportType
from src.core.util.helper.validator import Validator


class ReportFactory:

    __validator: Validator
    __settings: Settings

    def __init__(self):
        self.__validator = Validator()

    def provide_settings(self, settings: Settings):
        self.__validator.validate_type(settings, Settings)
        self.__settings = settings

    def __create_report(self, report_type: ReportType, reports_map: dict[ReportType, type]):
        (self.__validator.validate_type(report_type, ReportType)
         .validate_dict_types(reports_map, ReportType, type)
         .validate())

        reporter = reports_map[report_type]

        if reporter is None:
            raise NotImplementedError

        return reporter()

    def create_report(self, report_type: ReportType):
        return self.__create_report(report_type, self.__settings.reports_map)

    def create_default_report(self):
        return self.__create_report(self.__settings.report_default, self.__settings.reports_map)


