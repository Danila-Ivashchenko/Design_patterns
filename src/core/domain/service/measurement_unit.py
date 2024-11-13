from src.core.domain.repository.measurement_unit.repository import MeasurementUnitRepository
from src.core.domain.service.base.base import BaseService
from src.core.domain.service.filter import FilterService
from src.core.util.observer.event import Event


class MeasurementUnitService(BaseService):
    __measurement_unit_repository: MeasurementUnitRepository = None
    __filter_service: FilterService = None

    # to provide singleton
    __instance = None

    def __new__(cls, filter_service: FilterService):
        if cls.__instance is None:
            cls.__instance = super(MeasurementUnitService, cls).__new__(cls)

        return cls.__instance

    def __init__(self, filter_service: FilterService):
        super().__init__()

        self._validator.validate_type(filter_service, FilterService)
        self.__measurement_unit_repository = MeasurementUnitRepository()

    def get_all(self) -> list:
        return self.__measurement_unit_repository.find_all()

    def handle_event(self, event: Event):
        super().handle_event(event)