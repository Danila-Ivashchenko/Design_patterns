from .base import BaseReporter

class MarkDownReporter(BaseReporter):

    def report(self, data) -> str:
        if not isinstance(data, list):
            data = [data]

        markdown_lines = []
        data_properties = self._to_serializable(data)
        class_name = data[0].__class__.__name__
        flat_dicts = [self._to_serializable(item) for item in data_properties]

        for index, item_properties in enumerate(flat_dicts, 1):
            markdown_lines.append(f"## {class_name} {index}\n")
            for key, value in item_properties.items():
                if isinstance(value, list):
                    list_value = "\n"
                    for i, item in enumerate(value):
                        list_value += f"\t{item}\n"
                    markdown_lines.append(f"{key}: {list_value}")
                else:
                    markdown_lines.append(f"{key}: {value}")
            markdown_lines.append("\n---\n")

        return "\n".join(markdown_lines)