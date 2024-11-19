from src.core.domain.entity.storage_transaction import StorageTransaction
from src.core.domain.repository.base.datasource import BaseDataSource


class StorageTransactionDataSource(BaseDataSource[StorageTransaction]):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(StorageTransactionDataSource, cls).__new__(cls)
        return cls.__instance
