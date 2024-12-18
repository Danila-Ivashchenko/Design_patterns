import unittest as un

from src.core.domain.enums.report_type import ReportType
from src.core.domain.manager.setting_manager import SettingsManager
from src.infrastructure.data.generator.recipe import RecipeGenerator
from src.infrastructure.factory.report import ReportFactory
from src.infrastructure.report.xml_report import XmlReporter

manager = SettingsManager()
manager.open()
settings = manager.settings


class XmlReporterTests(un.TestCase):

    def test_report(self):
        report_type = ReportType.XML

        factory = ReportFactory(settings)
        reporter = factory.create_report(report_type)

        assert isinstance(reporter, XmlReporter)

        data = RecipeGenerator().get_base_recipes()
        report = reporter.report(data)

        with open(f'../reports/report.{report_type.name.lower()}', 'w', encoding='utf-8') as file:
            file.write(report)


