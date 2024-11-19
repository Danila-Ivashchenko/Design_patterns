from src.core.domain.entity.storage import Storage
from src.core.domain.repository.base.datasource import BaseDataSource


class StorageDataSource(BaseDataSource[Storage]):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(StorageDataSource, cls).__new__(cls)
        return cls.__instance