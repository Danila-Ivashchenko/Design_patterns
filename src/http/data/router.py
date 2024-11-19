from flask import Blueprint, request

from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.enums.event_type import EventType
from src.core.domain.service.dto.data.dump import DumpDTO
from src.core.domain.service.nomenclature import NomenclatureService
from src.di.helper import http_helper
from src.di.observer import observer
from src.di.service import nomenclature_service, recipe_service, filter_service, \
    measurement_unit_service, data_service, start_service, setting_manager


data_blueprint = Blueprint('/api/data', __name__, url_prefix='/api/data')

repository_data_sources = {
    "nomenclature": nomenclature_service,
    "recipe": recipe_service,
    "measurement_unit": measurement_unit_service
}


@data_blueprint.route('/api/data/<entity>', methods=['POST'])
def get_by_filter(entity):
    filter_data = request.json

    data = data_service.get_by_entity_name(entity)
    result = filter_service.get_by_entity_and_fiter_data(data, entity, filter_data)

    return http_helper.response_ok(result)


@data_blueprint.route('/api/data/dump', methods=['POST'])
def dump_data():
    data = request.json

    dto = http_helper.parse_request(DumpDTO, data)

    observer.notify(EventType.DUMP_DATA, dto.filename)
