from enums import ReportType
from .base import BaseReporter
from helper import Validator
from entity import Settings


class ReportFactory:

    _validator: Validator

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(ReportFactory, cls).__new__(cls)

        return cls.__instance

    def __init__(self):
        self._validator = Validator()

    def create_report(self, report_type: ReportType, reports_map: dict[ReportType, type]):
        (self._validator.validate_type(report_type, ReportType)
         .validate_dict_types(reports_map, ReportType, type)
         .validate())

        reporter = reports_map[report_type]

        if reporter is None:
            raise NotImplementedError

        return reporter()

    def create_default(self, settings: Settings):
        self._validator.validate_type(settings, Settings).validate()

        return self.create_report(settings.report_type, settings.report_map)


