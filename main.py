import helper
from service import StartService
from repository.recipe import RecipeRepository
from enums import ReportType
from manager import SettingsManager
from factory import ReportFactory, FilterFactory
from repository import DataRepository
from flask import request
import connexion

setting_manager = SettingsManager()
setting_manager.open('json/settings.json')

settings = setting_manager.settings
reports_factory = ReportFactory(settings)
filter_factory = FilterFactory()

data_repository = DataRepository()

start_service = StartService(data_repository)
http_helper = helper.HttpHelper()

app = connexion.FlaskApp(__name__)


@app.route('/api/reports/formats', methods=['GET'])
def report_types():
    return ReportType.list()


@app.route('/api/reports/<report_type>/entity/<entity>', methods=['GET'])
def get_report(report_type, entity):
    t = ReportType.from_int(report_type)

    if t is None:
        return 'report_type not found', 404

    reporter = reports_factory.create_report(t)

    units = start_service.get_by_unit_name(entity)

    return reporter.report(units)

@app.route('/api/data/<entity>', methods=['POST'])
def get_by_filter(entity):
    data = request.json

    result = start_service.get_by_entity_and_fiter_data(entity, data)

    return http_helper.response_ok(result)


if __name__ == '__main__':
    app.add_api('swagger.yaml')
    app.run(port=8080)