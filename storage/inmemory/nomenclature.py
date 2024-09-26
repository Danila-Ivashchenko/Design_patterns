from storage.base import InmemoryStorage
from entity import Nomenclature


class NomenclatureStorage(InmemoryStorage[str, Nomenclature]):
    def __init__(self):
        super().__init__()
