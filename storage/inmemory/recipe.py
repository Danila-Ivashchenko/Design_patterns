from entity import Recipe
from storage.base.inmemory import InmemoryStorage


class RecipeStorage(InmemoryStorage[str, Recipe]):
    def __init__(self):
        super().__init__()