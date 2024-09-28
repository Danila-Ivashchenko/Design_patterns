from .base import BaseReporter
from io import StringIO
import csv


class CsvReporter(BaseReporter):

    def __init__(self):
        super().__init__()

    def report(self, data):

        output = StringIO()

        writer = csv.writer(output)

        header = self._get_header(data)

        writer.writerow(header)

        rows = self._get_rows(data)

        for row in rows:
            writer.writerow(row)

        return output.getvalue()

    def _get_header(self, data):
        header = []

        if isinstance(data, list):
            if len(data) > 0:
                header = self._get_header_from_one(data[0])
        else:
            header = self._get_header_from_one(data)

        return header

    def _get_rows(self, data):
        rows = []

        if isinstance(data, list):
            rows = self._get_rows_from_list(data)
        else:
            rows = self._get_rows_from_one(data)

        return rows

    def _get_rows_from_list(self, data: list):
        self._validator.validate_type(data, list).validate_min_length(data, 0).validate()

        data_type = type(data[0])

        self._validator.validate_list_type(data, data_type).validate()

        result = []

        for item in data:
            result.append(self._get_rows_from_one(item))

        return result

    def _get_rows_from_one(self, data):
        fields = self._to_serializable(data)
        return [f'{str(field)}: {self._get_full_fields(getattr(data, field))}' for field in fields]

    def _get_header_from_one(self, data):
        return self._parser.parse_fields(data)

    def _get_full_fields(self, value, separator=";"):
        if isinstance(value, list):
            return "[" + separator.join(self._get_full_fields(v) for v in value) + "]"
        elif isinstance(value, dict):
            return separator.join(f'{"{"}{k}: {self._get_full_fields(v)}{"}"}' for k, v in value.items())
        else:
            return str(value)




