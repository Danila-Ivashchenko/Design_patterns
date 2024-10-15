from .base import BaseReporter

class RftDownReporter(BaseReporter):

    def report(self, data) -> str:
        if not isinstance(data, list):
            data = [data]

        class_name = data[0].__class__.__name__

        header = [
            r"{\rtf1\ansi\deff0",
            r"{\fonttbl{\f0\fswiss Arial;}}",
            r"\f0\fs24"
        ]

        body = []
        data_properties = self._to_serializable(data)


        for index, item_properties in enumerate([self._to_serializable(item) for item in data_properties], 1):
            body.append(f"\\b {class_name} {index}:\\b0 \\par")
            body.extend([f"\\b {key}:\\b0 {value} \\par" for key, value in item_properties.items()])
            body.append("\\par")

        total = header + body + ["}"]
        result = ''.join(total)

        return result

