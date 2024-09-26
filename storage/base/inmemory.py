from storage.base.base import BaseStorage, K, T
from helper import Validator


class InmemoryStorage(BaseStorage[K, T]):

    __data: {}
    _validator: Validator

    def __init__(self):
        self.__data = {}
        self._validator = Validator()

    def set(self, key: K, value: T):
        self.__data[key] = value

    def set_multiple(self, data: dict[K, T]):
        self.__data.update(data)

    def get(self, key: K) -> T:
        return self.__data[key]

    def get_all(self) -> list[T]:
        result = []

        for key in self.__data:
            result.append(self.__data[key])

        return result

    def contains(self, key: K) -> bool:
        self._validator.validate_type(key, K).validate()
        return key in self.__data

    def remove(self, key: K):
        self._validator.validate_type(key, K).validate()
        del self.__data[key]

    def remove_multiple(self, keys: list[K]):
        self._validator.validate_type(keys, list[K]).validate()
        for key in keys:
            del self.__data[key]

    def remove_all(self):
        self.__data = {}