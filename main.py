from flask import request
import connexion

from src.core.domain.abstract.typed_list import TypedList
from src.core.domain.service.dto.storage_turnover import StorageTurnoverDTO
from src.core.domain.service.dto.update_date_block_dto import UpdateDateBlockDTO
from src.core.domain.service.storage import StorageService
from src.core.util.helper.http import HttpHelper

from src.core.domain.enums.report_type import ReportType
from src.core.domain.service.setting_manager import SettingsManager
from src.core.domain.repository.data.data_repository import DataRepository
from src.core.domain.service.filter import FilterService
from src.core.domain.service.start import StartService
from src.di.factory import reports_factory
from src.di.service import setting_manager, start_service, filter_service, storage_service
from src.http.midllware import ExceptionMiddleware
from src.infrastructure.data.prototype.filter.entry.filter_entry import FilterEntry
from src.infrastructure.factory.filter import FilterFactory
from src.infrastructure.factory.prototipe import PrototypeFactory
from src.infrastructure.factory.report import ReportFactory


settings = setting_manager.settings

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

@app.route('/api/storage/turnover', methods=['POST'])
def storage_turnover():
    data = request.json

    storage_turnover_dto = http_helper.parse_request(StorageTurnoverDTO, data)
    result = storage_service.get_turnover(storage_turnover_dto)

    return http_helper.response_ok(result)


@app.route('/api/settings', methods=['GET'])
def get_settings():
    return http_helper.response_ok(setting_manager.settings)


@app.route('/api/settings/date_block', methods=['POST'])
def update_date_block():
    data = request.json

    dto = http_helper.parse_request(UpdateDateBlockDTO, data)

    storage_service.update_turnovers_by_date_block(dto.value)
    setting_manager.update_date_block(dto)
    setting_manager.save()
    return http_helper.response_ok(setting_manager.settings)


if __name__ == '__main__':
    app.add_api('swagger.yaml')
    app.add_wsgi_middleware(ExceptionMiddleware)
    app.run(port=8080)