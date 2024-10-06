import unittest as un
from enums import ReportType
import generator
from manager import SettingsManager
from report import JsonReporter
from factory import ReportFactory
from entity import Settings

manager = SettingsManager()
manager.open()
settings = manager.settings

class JsonReporterTests(un.TestCase):

    def test_report(self):
        report_type = ReportType.JSON

        factory = ReportFactory(settings)
        reporter = factory.create_report(report_type)

        data = generator.RecipeGenerator().get_base_recipes()
        report = reporter.report(data)

        with open(f'../reports/report.{report_type.name.lower()}', 'w', encoding='utf-8') as file:
            file.write(report)


