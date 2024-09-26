import report
from service import StartService
from repository.recipe import RecipeRepository

s = StartService(RecipeRepository())

recipes = s.get_all_recipes

reporter = report.JsonReporter()

print(reporter.report(recipes[0]))

