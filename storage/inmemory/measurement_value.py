from storage.base import InmemoryStorage
from entity import MeasurementValue


class MeasurementValueStorage(InmemoryStorage[str, MeasurementValue]):
    def __init__(self):
        super().__init__()