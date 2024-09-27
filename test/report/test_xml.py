import unittest as un
from enums import ReportType
import generator
from report import XmlReporter
from factory import ReportFactory
from entity import Settings

settings = Settings()

class XmlReporterTests(un.TestCase):

    def test_report(self):
        report_type = ReportType.XML

        factory = ReportFactory()
        reporter = factory.create_report(report_type, settings)

        data = generator.RecipeGenerator().get_base_recipes()
        report = reporter.report(data)

        with open(f'../reports/report.{report_type.name.lower()}', 'w', encoding='utf-8') as file:
            file.write(report)


