from enums import ReportType
from entity import Settings
from helper import Validator


class ReportFactory:

    _validator: Validator

    def __init__(self):
        self._validator = Validator()

    def _create_report(self, report_type: ReportType, reports_map: dict[ReportType, type]):
        (self._validator.validate_type(report_type, ReportType)
         .validate_dict_types(reports_map, ReportType, type)
         .validate())

        reporter = reports_map[report_type]

        if reporter is None:
            raise NotImplementedError

        return reporter()

    def create_report(self, report_type: ReportType, settings: Settings):
        return self._create_report(report_type, settings.report_map)

    def create_default_report(self, settings: Settings):
        return self._create_report(settings.report_type, settings.report_map)


