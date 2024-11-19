from flask import Blueprint, request

from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.enums.event_type import EventType
from src.core.domain.service.dto.data.dump import DumpDTO
from src.core.domain.service.dto.osv.get import OsvGetDTO
from src.core.domain.service.nomenclature import NomenclatureService
from src.di.helper import http_helper
from src.di.observer import observer
from src.di.service import nomenclature_service, recipe_service, filter_service, \
    measurement_unit_service, data_service, start_service, setting_manager, osv_service

osv_blueprint = Blueprint('/api/osv', __name__, url_prefix='/api/osv')

@osv_blueprint.route('', methods=['GET'])
def get():

    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    storage_id = request.args.get("storage_id")

    start_date = int(start_date)
    end_date = int(end_date)

    dto = OsvGetDTO()

    if storage_id is not None:
        dto.storage_id = storage_id

    dto.start_date = start_date
    dto.end_date = end_date

    result = osv_service.get(dto)

    return http_helper.response_ok(result)
