from src.core.domain.entity.measurement_unit import MeasurementUnit
from src.core.domain.repository.base.datasource import BaseDataSource


class MeasurementUnitDataSource(BaseDataSource[MeasurementUnit]):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(MeasurementUnitDataSource, cls).__new__(cls)
        return cls.__instance