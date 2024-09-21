from abc import ABC, abstractmethod
from entity import Recipe


class IRecipeRepository(ABC):
    @abstractmethod
    def create(self, data: Recipe):
        pass

    @abstractmethod
    def create_multiple(self, data: list[Recipe]):
        pass

    @abstractmethod
    def update(self, data: Recipe):
        pass

    @abstractmethod
    def update_multiple(self, data: list[Recipe]):
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> Recipe:
        pass

    @abstractmethod
    def find_all(self) -> list[Recipe]:
        pass

    @abstractmethod
    def delete(self, id: str):
        pass

    @abstractmethod
    def delete_multiple(self, ids: list[str]):
        pass