from src.core.domain.service.base.base import BaseService
from src.infrastructure.factory.filter import FilterFactory
from src.infrastructure.factory.prototipe import PrototypeFactory
from src.core.domain.errors.abstract import AbstractException


class FilterService(BaseService):

    __filter_factory: FilterFactory
    __prototype_factory: PrototypeFactory

    def __init__(self, filter_factory: FilterFactory, prototype_factory: PrototypeFactory):
        super().__init__()

        self._validator.validate_type(filter_factory, FilterFactory)
        self._validator.validate_type(prototype_factory, PrototypeFactory)
        self._validator.validate()

        self.__filter_factory = filter_factory
        self.__prototype_factory = prototype_factory

    def get_by_entity_and_fiter_data(self, data: list, entity_name: str, filter_data: dict):
        self._validator.validate_type(entity_name, str).validate_type(filter_data, dict)
        self._validator.validate_type(data, list)

        try:
            self._validator.validate()

            filter_dto = self.__filter_factory.create_filter(entity_name, filter_data)
            prototype = self.__prototype_factory.create_prototype(entity_name, data)

            return prototype.create(filter_dto)
        except AbstractException as e:
            self.set_error(e)
