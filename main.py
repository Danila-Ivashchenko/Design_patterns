from service import StartService
from repository.recipe import RecipeRepository

s = StartService(RecipeRepository())

recipes = s.get_all_recipes

for recipe in recipes:
    print()

    for ingredient in recipe.ingredients:
        print(ingredient)

    print()

    for step in recipe.steps:
        print(step)
