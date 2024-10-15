import helper
from service import StartService, FilterService
from repository.recipe import RecipeRepository
from enums import ReportType
from manager import SettingsManager
from factory import ReportFactory, FilterFactory, PrototypeFactory
from repository import DataRepository
from flask import request
import connexion

setting_manager = SettingsManager()
setting_manager.open('json/settings.json')

settings = setting_manager.settings
reports_factory = ReportFactory(settings)
filter_factory = FilterFactory()
prototype_factory = PrototypeFactory()

data_repository = DataRepository()

start_service = StartService(data_repository)
filter_service = FilterService(filter_factory, prototype_factory)
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
    filter_data = request.json

    data = start_service.get_by_unit_name(entity)
    result = filter_service.get_by_entity_and_fiter_data(data, entity, filter_data)

    return http_helper.response_ok(result)


if __name__ == '__main__':
    app.add_api('swagger.yaml')
    app.run(port=8080)