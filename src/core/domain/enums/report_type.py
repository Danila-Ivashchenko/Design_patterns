from enum import Enum


class ReportType(Enum):
    CSV = 1
    MARKDOWN = 2
    JSON = 3
    XML = 4
    RTF = 5

    @staticmethod
    def list():
        result = {}
        for item in ReportType:
            result[item.name] = item.value

        return result

    @staticmethod
    def from_int(value):
        for item in ReportType:
            if item.value == value:
                return item
        return None

