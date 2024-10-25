from flask import request
import connexion

from src.core.domain.abstract.typed_list import TypedList
from src.core.domain.service.dto.storage_turnover import StorageTurnoverDTO
from src.core.domain.service.storage import StorageService
from src.core.util.helper.http import HttpHelper

from src.core.domain.enums.report_type import ReportType
from src.core.domain.manager.setting_manager import SettingsManager
from src.core.domain.repository.data.data_repository import DataRepository
from src.core.domain.service.filter import FilterService
from src.core.domain.service.start import StartService
from src.infrastructure.data.prototype.filter.entry.filter_entry import FilterEntry
from src.infrastructure.factory.filter import FilterFactory
from src.infrastructure.factory.prototipe import PrototypeFactory
from src.infrastructure.factory.report import ReportFactory

setting_manager = SettingsManager()
setting_manager.open('json/settings.json')

settings = setting_manager.settings
reports_factory = ReportFactory(settings)
filter_factory = FilterFactory()
prototype_factory = PrototypeFactory()

data_repository = DataRepository()

start_service = StartService(data_repository)
filter_service = FilterService(filter_factory, prototype_factory)
storage_service = StorageService(data_repository, filter_service)

http_helper = HttpHelper()
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

@app.route('/api/storage/turnover', methods=['POST'])
def storage_turnover():
    data = request.json

    storage_turnover_dto = http_helper.parse_request(StorageTurnoverDTO, data)
    result = storage_service.get_turnover(storage_turnover_dto)

    return http_helper.response_ok(result)


if __name__ == '__main__':
    app.add_api('swagger.yaml')
    app.run(port=8080)