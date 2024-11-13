from src.core.domain.entity.nomenclature_group import NomenclatureGroup
from src.core.domain.repository.base.datasource import BaseDataSource


class NomenclatureGroupDataSource(BaseDataSource[NomenclatureGroup]):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(NomenclatureGroupDataSource, cls).__new__(cls)
        return cls.__instance