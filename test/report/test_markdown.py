import unittest as un
from enums import ReportType
import generator
from report import ReportFactory, MarkDownReporter

reports_map = {
    ReportType.MARKDOWN: MarkDownReporter
}

class MarkDownReporterTests(un.TestCase):

    def test_report(self):
        report_type = ReportType.MARKDOWN

        factory = ReportFactory()
        reporter = factory.create_report(report_type, reports_map)

        data = generator.RecipeGenerator().get_base_recipes()
        report = reporter.report(data[0])

        with open(f'../reports/report.{report_type.name.lower()}', 'w', encoding='utf-8') as file:
            file.write(report)



