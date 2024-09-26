from abc import ABC, abstractmethod
from typing import TypeVar, Generic


# key type
K = TypeVar('K')

# value type
T = TypeVar('T')


class BaseStorage(ABC, Generic[K, T]):
    @abstractmethod
    def set(self, key: K, value: T):
        ...

    @abstractmethod
    def set_multiple(self, data: dict[K, T]):
        ...

    @abstractmethod
    def get(self, key: K) -> T:
        ...

    @abstractmethod
    def get_all(self) -> dict[K, T]:
        ...

    @abstractmethod
    def contains(self, key: K) -> bool:
        ...

    @abstractmethod
    def remove(self, key: K):
        ...

    @abstractmethod
    def remove_multiple(self, keys: list[K]):
        ...

    @abstractmethod
    def remove_all(self):
        ...