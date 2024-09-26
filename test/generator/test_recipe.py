from generator import RecipeGenerator
from entity import Recipe
import unittest as un

from main import recipes


class RecipeGeneratorTests(un.TestCase):

    def test_creating(self):
        gen = RecipeGenerator()

        recipes = gen.get_base_recipes()

        for recipe in recipes:
            assert type(recipe) is Recipe
            assert len(recipe.steps) > 0
            assert len(recipe.ingredients) > 0
            assert len(recipe.name) > 0
            assert recipe.name is not None