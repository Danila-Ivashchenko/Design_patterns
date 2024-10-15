import unittest as un

from src.core.domain.entity.settings import Settings
from src.core.domain.enums.report_type import ReportType
from src.infrastructure.data.generator.recipe import RecipeGenerator
from src.infrastructure.factory.report import ReportFactory

settings = Settings()


class RftReporterTests(un.TestCase):

    def test_report(self):
        report_type = ReportType.RTF

        factory = ReportFactory()
        reporter = factory.create_report(report_type, settings)

        data = RecipeGenerator().get_base_recipes()
        report = reporter.report(data)

        with open(f'../reports/report.{report_type.name.lower()}', 'w', encoding='utf-8') as file:
            file.write(report)


