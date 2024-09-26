from .base import BaseReporter

class MarkDownReporter(BaseReporter):

    def report(self, data):
        markdown_lines = []

        if not isinstance(data, list):
            data = [data]

        flat_dicts = [self._to_serializable(item) for item in data]

        class_name = self._get_main_class_name(data)

        for i, flat_dict in enumerate(flat_dicts, 1):
            markdown_lines.append(f"### {class_name} {i}\n")
            for key, value in flat_dict.items():
                markdown_lines.append(f"**{key}**: {value}")
            markdown_lines.append("\n---\n")

        return "\n".join(markdown_lines)