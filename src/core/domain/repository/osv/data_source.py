from src.core.domain.entity.osv import Osv
from src.core.domain.repository.base.datasource import BaseDataSource


class OsvDataSource(BaseDataSource[Osv]):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(OsvDataSource, cls).__new__(cls)
        return cls.__instance