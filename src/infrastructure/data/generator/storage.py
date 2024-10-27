from src.infrastructure.data.generator.base import BaseGenerator
from src.core.domain.entity.storage import Storage


class StorageGenerator(BaseGenerator):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StorageGenerator, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()

        self.__generate()

    def __generate(self):
        self.__main_storage = Storage()
        self.__main_storage.name = "Основной склад"
        self.__main_storage.location = "Улица Ленина, 1"

        self.__secondary_storage = Storage()
        self.__secondary_storage.name = "Второй склад"
        self.__secondary_storage.location = "Улица Ленина, 2"

    @property
    def main_storage(self):
        return self.__main_storage

    @property
    def secondary_storage(self):
        return self.__secondary_storage

    @property
    def list(self):
        return [self.main_storage, self.secondary_storage]
