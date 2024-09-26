from enum import Enum

class ReportType(Enum):
    CSV = 1
    MARKDOWN = 2
    JSON = 3
    XML = 4
    RTF = 5


class ReportTypeMapper:

    @staticmethod
    def from_int_type(report_type: int):
        if report_type == 1:
            return ReportType.CSV
        elif report_type == 2:
            return ReportType.MARKDOWN
        elif report_type == 3:
            return ReportType.JSON
        elif report_type == 4:
            return ReportType.XML
        elif report_type == 5:
            return ReportType.RTF
        raise NotImplementedError

    @staticmethod
    def from_str_type(report_type: str):
        if report_type == "CSV":
            return ReportType.CSV
        elif report_type == "MARKDOWN":
            return ReportType.MARKDOWN
        elif report_type == "JSON":
            return ReportType.JSON
        elif report_type == "XML":
            return ReportType.XML
        elif report_type == "RTF":
            return ReportType.RTF
        raise NotImplementedError
