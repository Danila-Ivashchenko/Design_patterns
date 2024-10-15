from helper import JsonHelper
from entity import NomenclatureGroup, Nomenclature, Ingredient, MeasurementUnit, Recipe
from typing import List
from abstract import TypedList
from generator import RecipeGenerator
import unittest as un
from repository import DataRepository
from service import StartService
from prototype import NomenclaturePrototype, NomenclatureFilter, OperationEnum, FilterEntry


class JsonHelperTests(un.TestCase):
    def test_desirilize_nomenclatura_group(self):
        data = {
            "id": "uuid",
            "name": "мясо"
        }

        helper = JsonHelper()

        res = helper.to_deserialize(NomenclatureGroup, data)

        assert res.id == data["id"]
        assert res.name == data["name"]

    def test_desirilize_nomenclature(self):
        data = {
            "id": "8aa73f1f-b773-49ce-bbfb-43c382973b82",
            "measurement_uint": {
                "id": "2e5e899c-87c7-4984-8335-644b8bcbbd37",
                "name": "штука",
                "parent_unit": None,
                "ratio": 1.0
            },
            "name": "яйца",
            "nomenclature_group_id": "945a4893-3762-4cdb-97fb-da181448bc82"
        }

        helper = JsonHelper()

        res = helper.to_deserialize(Nomenclature, data)

        assert res.id == data["id"]
        assert res.name == data["name"]
        assert res.nomenclature_group_id == data["nomenclature_group_id"]
        assert res.measurement_uint.id == data["measurement_uint"]["id"]
        assert res.measurement_uint.name == data["measurement_uint"]["name"]
        assert res.measurement_uint.parent_unit == data["measurement_uint"]["parent_unit"]
        assert res.measurement_uint.ratio == data["measurement_uint"]["ratio"]

    def test_desirilize_ingredient(self):
        data = {
            "id": "c317238f-f06e-4675-9b00-fe81f8ecc1b5",
            "measurement_value": {
                "id": "65e7ad62-98a0-45e2-9465-8a2b9fc401b4",
                "unit": {
                    "id": "8c8959e8-0d40-4a92-a342-31b7e9a7e0a1",
                    "name": "десяток",
                    "parent_unit": {
                            "id": "8c8959e8-0d40-4a92-a342-31b7e9a7e0a1",
                            "name": "штука",
                            "parent_unit": None,
                            "ratio": 1.0
                    },
                    "ratio": 10.0
                },
                "value": 3.0
            },
            "nomenclature": {
                "id": "f954f284-c4a2-42d8-bf15-4b10450c8da1",
                "measurement_uint": {
                    "id": "8c8959e8-0d40-4a92-a342-31b7e9a7e0a1",
                    "name": "десяток",
                    "parent_unit": {
                            "id": "8c8959e8-0d40-4a92-a342-31b7e9a7e0a1",
                            "name": "штука",
                            "parent_unit": None,
                            "ratio": 1.0
                    },
                    "ratio": 10.0
                },
                "name": "яйца",
                "nomenclature_group_id": "a9b45996-ad74-44d2-a3a6-f112ad434e01"
            }
        }

        helper = JsonHelper()

        res = helper.to_deserialize(Ingredient, data)

        assert res is not None
        assert res.id == data["id"]
        assert res.nomenclature.id == data["nomenclature"]["id"]
        assert res.nomenclature.name == data["nomenclature"]["name"]
        assert res.nomenclature.nomenclature_group_id == data["nomenclature"]["nomenclature_group_id"]

        assert res.nomenclature.measurement_uint.id == data["nomenclature"]["measurement_uint"]["id"]
        assert res.nomenclature.measurement_uint.name == data["nomenclature"]["measurement_uint"]["name"]
        assert res.nomenclature.measurement_uint.ratio == data["nomenclature"]["measurement_uint"]["ratio"]
        assert res.nomenclature.measurement_uint.parent_unit.id == data["nomenclature"]["measurement_uint"]["parent_unit"]["id"]
        assert res.nomenclature.measurement_uint.parent_unit.id == data["nomenclature"]["measurement_uint"]["parent_unit"]["id"]
        assert res.nomenclature.measurement_uint.parent_unit.name == data["nomenclature"]["measurement_uint"]["parent_unit"]["name"]
        assert res.nomenclature.measurement_uint.parent_unit.ratio == data["nomenclature"]["measurement_uint"]["parent_unit"]["ratio"]

        assert res.measurement_value.unit.id == data["measurement_value"]["unit"]["id"]
        assert res.measurement_value.unit.name == data["measurement_value"]["unit"]["name"]
        assert res.measurement_value.unit.ratio == data["measurement_value"]["unit"]["ratio"]
        assert res.measurement_value.unit.parent_unit.id == data["measurement_value"]["unit"]["parent_unit"]["id"]
        assert res.measurement_value.unit.parent_unit.id == data["measurement_value"]["unit"]["parent_unit"]["id"]
        assert res.measurement_value.unit.parent_unit.name == data["measurement_value"]["unit"]["parent_unit"]["name"]
        assert res.measurement_value.unit.parent_unit.ratio == data["measurement_value"]["unit"]["parent_unit"]["ratio"]

    def test_recipe(self):

        recipe_generator = RecipeGenerator()

        recipe = recipe_generator.get_base_recipes()[0]

        helper = JsonHelper()
        recipe_dict = helper.to_serialize(recipe)

        res = helper.to_deserialize(Recipe, recipe_dict)

        res_dict = helper.to_serialize(res)

        assert res_dict == recipe_dict

    def test_recipes(self):
        recipe_generator = RecipeGenerator()

        recipes = recipe_generator.get_base_recipes()
        recipes = TypedList(Recipe, recipes)

        helper = JsonHelper()
        recipes_dict = helper.to_serialize(recipes)

        res = helper.to_deserialize(TypedList(Recipe), recipes_dict)

        assert len(res) == len(recipes)

        for i, recipe in enumerate(res):
            src_recipe = recipes[i]

            assert recipe.id == src_recipe.id
            assert recipe.name == src_recipe.name
            assert len(recipe.steps) == len(src_recipe.steps)
            assert len(recipe.ingredients) == len(src_recipe.ingredients)

            for j, ingredient in enumerate(recipe.ingredients):
                src_ingredient = src_recipe.ingredients[j]

                assert ingredient.id == src_ingredient.id
                assert ingredient.nomenclature.id == src_ingredient.nomenclature.id
                assert ingredient.nomenclature.name == src_ingredient.nomenclature.name
                assert ingredient.nomenclature.nomenclature_group_id == src_ingredient.nomenclature.nomenclature_group_id
                assert ingredient.nomenclature.measurement_uint.id == src_ingredient.nomenclature.measurement_uint.id
                assert ingredient.nomenclature.measurement_uint.ratio == src_ingredient.nomenclature.measurement_uint.ratio
                assert ingredient.nomenclature.measurement_uint.parent_unit == src_ingredient.nomenclature.measurement_uint.parent_unit

            for j, step in enumerate(recipe.steps):
                src_step = src_recipe.steps[j]

                assert step == src_step

    def test_prototype(self):
        data_repository = DataRepository()
        start_service = StartService(data_repository)

        data = start_service.get_all_nomenclature
        prot = NomenclaturePrototype(data)

        filter_nomenclature = NomenclatureFilter()
        filter_nomenclature.name = FilterEntry("масло", OperationEnum.Like)
        # filter_nomenclature.name_operation(OperationEnum.Like)

        helper = JsonHelper()

        res = helper.to_serialize(filter_nomenclature)

        assert res is not None

        new_filter = helper.to_deserialize(NomenclatureFilter, res)

        assert new_filter.name.value ==  filter_nomenclature.name.value
        assert new_filter.name.operation ==  filter_nomenclature.name.operation

        assert new_filter.id ==  filter_nomenclature.id

