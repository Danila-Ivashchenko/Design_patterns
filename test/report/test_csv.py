import unittest as un
from enums import ReportType
from entity import Settings
import generator
from report import CssvReporter
from factory import ReportFactory

settings = Settings()



class CsvReporterTests(un.TestCase):

    def test_report(self):
        report_type = ReportType.CSV

        factory = ReportFactory()
        reporter = factory.create_report(report_type, settings)

        data = generator.RecipeGenerator().get_base_recipes()
        report = reporter.report(data)

        with open(f'../reports/report.{report_type.name.lower()}', 'w', encoding='utf-8') as file:
            file.write(report)


