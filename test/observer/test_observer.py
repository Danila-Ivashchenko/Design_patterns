import unittest as un

from src.core.domain.repository.data.data_repository import DataRepository
from src.core.domain.repository.nomenclature.repository import NomenclatureRepository
from src.core.domain.repository.recipe.repository import RecipeRepository
from src.core.domain.service.dto.nomenclature.update import UpdateNomenclatureDTO
from src.core.domain.service.filter import FilterService
from src.core.domain.service.nomenclature import NomenclatureService
from src.core.domain.service.recipe import RecipeService
from src.core.domain.service.start import StartService

from src.core.util.observer.observer import Observer
from src.infrastructure.data.generator.nomenclature import NomenclatureGenerator
from src.infrastructure.factory.filter import FilterFactory
from src.infrastructure.factory.prototipe import PrototypeFactory

filter_factory = FilterFactory()
prototype_factory = PrototypeFactory()

data_repository = DataRepository()
start_service = StartService(data_repository)
filter_service = FilterService(filter_factory, prototype_factory)

nomenclature_generator = NomenclatureGenerator()

class ObserverTest(un.TestCase):

    def test_observer(self):

        # Arrange
        observer = Observer()

        nomenclature_service = NomenclatureService(filter_service)

        recipe_service = RecipeService(filter_service)

        observer.register(recipe_service)

        recipe_repository = RecipeRepository()

        # Act

        cur_item = nomenclature_generator.egs

        update_nomenclature_dto = UpdateNomenclatureDTO()

        update_nomenclature_dto.id = cur_item.id
        update_nomenclature_dto.name = "test"

        nomenclature_service.update(update_nomenclature_dto)

        # Assert

        all_recipes = recipe_repository.find_all()

        for recipe in all_recipes:
            for ingredient in recipe.ingredients:
                if ingredient.nomenclature.id == cur_item.id:
                    assert ingredient.nomenclature.name == "test"
