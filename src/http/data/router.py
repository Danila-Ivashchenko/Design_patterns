from flask import Blueprint, request

from src.core.domain.entity.nomenclature import Nomenclature
from src.core.domain.service.nomenclature import NomenclatureService
from src.di.helper import http_helper
from src.di.service import nomenclature_service, recipe_service, start_service, filter_service

data_blueprint = Blueprint('/api/data', __name__, url_prefix='/api/data')

repository_data_sources = {
    "nomenclature": nomenclature_service,
    "recipe": recipe_service,
}


def get_data_from_source(entity):
    result = []

    if entity in repository_data_sources:
        result = repository_data_sources[entity].get_all()
    else:
        result = start_service.get_by_unit_name(entity)

    return result


@data_blueprint.route('/api/data/<entity>', methods=['POST'])
def get_by_filter(entity):
    filter_data = request.json

    data = get_data_from_source(entity)
    result = filter_service.get_by_entity_and_fiter_data(data, entity, filter_data)

    return http_helper.response_ok(result)
