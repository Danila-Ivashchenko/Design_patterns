import unittest as un

from src.core.domain.repository.data.data_repository import DataRepository
from src.core.domain.service.data import DataService
from src.core.domain.service.filter import FilterService
from src.core.domain.service.start import StartService

from src.infrastructure.data.generator.nomenclature import NomenclatureGenerator
from src.infrastructure.factory.filter import FilterFactory
from src.infrastructure.factory.prototipe import PrototypeFactory

filter_factory = FilterFactory()
prototype_factory = PrototypeFactory()

data_repository = DataRepository()
start_service = StartService(data_repository)
filter_service = FilterService(filter_factory, prototype_factory)

nomenclature_generator = NomenclatureGenerator()


def assert_nomenclature_equal(nomenclature_1, nomenclature_2):
    assert nomenclature_1.name == nomenclature_2.name
    assert nomenclature_1.nomenclature_group_id == nomenclature_2.nomenclature_group_id
    assert nomenclature_1.measurement_unit == nomenclature_2.measurement_unit

    assert nomenclature_1.id == nomenclature_2.id


def assert_nomenclature_group_equal(nomenclature_group_1, nomenclature_group_2):
    assert nomenclature_group_1.name == nomenclature_group_2.name


def assert_measurement_unit_equal(measurement_unit_1, measurement_unit_2):
    assert measurement_unit_1.name == measurement_unit_2.name
    assert measurement_unit_1.parent_unit == measurement_unit_2.parent_unit
    assert measurement_unit_1.ratio == measurement_unit_2.ratio
    assert measurement_unit_1.parent_unit == measurement_unit_2.parent_unit


def assert_measurement_value(measurement_value_1, measurement_value_2):
    assert measurement_value_1.value == measurement_value_2.value
    assert measurement_value_1.unit == measurement_value_2.unit
    assert measurement_value_1.id == measurement_value_2.id


def assert_ingredient_equal(ingredient_1, ingredient_2):
    assert ingredient_1.id == ingredient_2.id
    assert_nomenclature_equal(ingredient_1.nomenclature, ingredient_2.nomenclature)
    assert_measurement_value(ingredient_1.measurement_value, ingredient_2.measurement_value)


def assert_recipe_equal(recipe_1, recipe_2):
    assert recipe_1.name == recipe_2.name
    for ingredient_1, ingredient_2 in zip(recipe_1.ingredients, recipe_2.ingredients):
        assert_ingredient_equal(ingredient_1, ingredient_2)

    assert recipe_1.time == recipe_2.time
    for step_1, step_2 in zip(recipe_1.steps, recipe_2.steps):
        assert step_1 == step_2



class DataServiceTest(un.TestCase):

    def test_dump(self):

        # Arrange

        data_service = DataService()

        # Act

        json_data = data_service.dump_json()

        from_json_data = data_service.from_json(json_data)

        # Assert

        assert json_data is not None
        assert from_json_data is not None

        assert len(json_data['nomenclature']) == len(from_json_data['nomenclature'])

    def test_dump_nomenclature(self):

        # Arrange

        data_service = DataService()

        # Act

        json_data = data_service.dump_json()

        from_json_data = data_service.from_json(json_data)

        # Assert

        assert json_data is not None
        assert from_json_data is not None

        assert len(json_data['nomenclature']) == len(from_json_data['nomenclature'])
        all_nomenclatures = data_service.get_by_entity_name('nomenclature')

        for nomenclature in from_json_data['nomenclature']:
            existed_nomenclature = None

            for all_nomenclature in all_nomenclatures:
                if all_nomenclature.id == nomenclature.id:
                    existed_nomenclature = all_nomenclature
                    break

            assert existed_nomenclature is not None

            assert_nomenclature_equal(existed_nomenclature, nomenclature)

    def test_dump_measurement_unit(self):

        # Arrange

        data_service = DataService()

        # Act

        json_data = data_service.dump_json()

        from_json_data = data_service.from_json(json_data)

        # Assert

        assert json_data is not None
        assert from_json_data is not None

        assert len(json_data['measurement_unit']) == len(from_json_data['measurement_unit'])
        all_measurement_units = data_service.get_by_entity_name('measurement_unit')

        for measurement_unit in from_json_data['measurement_unit']:
            existed_measurement_unit = None

            for all_measurement_unit in all_measurement_units:
                if measurement_unit.id == all_measurement_unit.id:
                    existed_measurement_unit = all_measurement_unit
                    break

            assert existed_measurement_unit is not None

            assert_measurement_unit_equal(existed_measurement_unit, measurement_unit)

    def test_dump_recipe(self):

        # Arrange

        data_service = DataService()

        # Act

        json_data = data_service.dump_json()

        from_json_data = data_service.from_json(json_data)

        # Assert

        assert json_data is not None
        assert from_json_data is not None

        assert len(json_data['recipe']) == len(from_json_data['recipe'])
        all_recipes = data_service.get_by_entity_name('recipe')

        for recipe in from_json_data['recipe']:
            existed_recipe = None

            for all_recipe in all_recipes:
                if recipe.id == all_recipe.id:
                    existed_recipe = all_recipe
                    break

            assert recipe is not None

            assert_recipe_equal(existed_recipe, recipe)









