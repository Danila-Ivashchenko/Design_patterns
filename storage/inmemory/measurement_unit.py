from storage.base import InmemoryStorage
from entity import MeasurementUnit


class MeasurementUnitStorage(InmemoryStorage[str, MeasurementUnit]):
    def __init__(self):
        super().__init__()