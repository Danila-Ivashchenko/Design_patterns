from .base import BaseReporter
import json


class JsonReporter(BaseReporter):

    def __init__(self):
        super().__init__()

    @staticmethod
    def class_name():
        return 'JsonReporter'

    def report(self, data):
        data = self._to_serializable(data)

        return json.dumps(data, indent=4, ensure_ascii=False)


