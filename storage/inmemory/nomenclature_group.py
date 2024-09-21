from storage.base import InmemoryStorage
from entity import NomenclatureGroup


class NomenclatureGroupStorage(InmemoryStorage[str, NomenclatureGroup]):
    def __init__(self):
        super().__init__()