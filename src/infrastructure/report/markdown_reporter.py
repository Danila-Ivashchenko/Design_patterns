from .base import BaseReporter

class MarkDownReporter(BaseReporter):

    def report(self, data: list) -> str:
        if not isinstance(data, list):
            data = [data]

        markdown = "# Report\n\n"

        for i, d in enumerate(data):
            markdown += f"## {d.__class__.__name__} {i}\n\n"
            fields = self._to_serializable(d)

            for field in fields:
                value = self._to_serializable(getattr(d, field))
                markdown += f"### {field.capitalize()}\n"

                markdown += self._get_right_markup(value) + "\n-------------\n"

        return markdown

    def _get_right_markup(self, value):
        if isinstance(value, list):
            return '\n'.join(f"- {self._get_right_markup(v)}" for v in value)
        elif isinstance(value, dict):
            return '\n'.join(f"**{k}**: {self._get_right_markup(v)}" for k, v in value.items())
        else:
            return str(value)



