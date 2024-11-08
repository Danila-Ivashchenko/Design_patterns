from flask import Blueprint, request

from src.core.domain.errors.not_found import NotFoundException
from src.core.domain.service.dto.nomenclature.create import CreateNomenclatureDTO
from src.core.domain.service.dto.nomenclature.update import UpdateNomenclatureDTO
from src.core.domain.service.nomenclature import NomenclatureService
from src.di.helper import http_helper
from src.di.service import nomenclature_service
from src.http.midllware import ExceptionMiddleware

nomenclature_blueprint = Blueprint('/api/nomenclature', __name__, url_prefix='/api/nomenclature')


@nomenclature_blueprint.route('/<id>', methods=['GET'])
def get_nomenclature_by_id(id):
    result = nomenclature_service.get_by_id(id)

    if result == None:
        raise NotFoundException.not_found_entity_by_id("nomenclature", id)

    return http_helper.response_ok(result)

@nomenclature_blueprint.route('/', methods=['PUT'])
def create_nomenclature():
    data = request.json

    dto = http_helper.parse_request(CreateNomenclatureDTO, data)

    result = nomenclature_service.create(dto)

    return http_helper.response_ok(result)

@nomenclature_blueprint.route('/<id>', methods=['PATCH'])
def update_nomenclature(id):
    data = request.json

    dto = http_helper.parse_request(UpdateNomenclatureDTO, data)

    dto.id = id

    result = nomenclature_service.update(dto)

    return http_helper.response_ok(result)

@nomenclature_blueprint.route('/<id>', methods=['DELETE'])
def delete_nomenclature(id):
    result = nomenclature_service.delete(id)

    return http_helper.response_ok(result)