from src.core.domain.service.data import DataService
from src.core.domain.service.filter import FilterService
from src.core.domain.service.measurement_unit import MeasurementUnitService
from src.core.domain.service.nomenclature import NomenclatureService
from src.core.domain.service.recipe import RecipeService
from src.core.domain.service.setting_manager import SettingsManager
from src.core.domain.service.start import StartService
from src.core.domain.service.storage import StorageService
from src.di.factory import filter_factory, prototype_factory, reports_factory
from src.di.observer import observer
from src.di.repository import data_repository

setting_manager = SettingsManager()
setting_manager.open('json/settings.json')
start_service = StartService(data_repository)
filter_service = FilterService(filter_factory, prototype_factory)

nomenclature_service = NomenclatureService(filter_service)
recipe_service = RecipeService(filter_service)
storage_service = StorageService(data_repository, filter_service, setting_manager)
measurement_unit_service = MeasurementUnitService(filter_service)

data_service = DataService(start_service)

data_service.dump_json()

storage_service.init_turnovers_by_date_block(setting_manager.settings.date_block)


reports_factory.provide_settings(setting_manager.settings)

observer.register(nomenclature_service)
observer.register(recipe_service)