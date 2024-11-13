import typing

from src.core.domain.entity.base import BaseEntity

T = typing.TypeVar('T', bound=BaseEntity)


class BaseDataSource(typing.Generic[T]):

    def __init__(self):
        self.__data = {}

    def create(self, data: T) -> T:
        self.__data[data.id] = data

        return data

    def get_all(self) -> list[T]:
        return list(self.__data.values())

    def get_by_id(self, id: str) -> T | None:
        result = None

        if id in self.__data:
            result = self.__data[id]

        return result

    def create_multiple(self, nomenclatures: list[T]) -> list[T]:
        result = []

        for nomenclature in nomenclatures:
            result.append(self.create(nomenclature))

        return result

    def delete(self, id: str):
        if id in self.__data:
            del self.__data[id]