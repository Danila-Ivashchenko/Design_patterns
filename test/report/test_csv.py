import unittest as un
from enums import ReportType
from manager import SettingsManager
from entity import Settings
import generator
from report import CsvReporter
from factory import ReportFactory

manager = SettingsManager()
manager.open()
settings = manager.settings


class CsvReporterTests(un.TestCase):

    def test_report(self):
        report_type = ReportType.CSV

        factory = ReportFactory(settings)
        reporter = factory.create_report(report_type)

        assert isinstance(reporter, CsvReporter)

        data = generator.RecipeGenerator().get_base_recipes()
        report = reporter.report(data)

        with open(f'../reports/report.{report_type.name.lower()}', 'w', encoding='utf-8') as file:
            file.write(report)


