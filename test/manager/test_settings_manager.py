
import unittest as un

from src.core.domain.errors import OperationException
from src.core.domain.manager.setting_manager import SettingsManager


class TestSettingsManager(un.TestCase):
    def test_is_singleton(self):
        settings_manager1 = SettingsManager()
        settings_manager1.open("json/settings_1.json")

        settings_manager2 = SettingsManager()
        settings_manager2.open("json/settings_2.json")

        settings1 = settings_manager1.settings
        settings2 = settings_manager2.settings

        assert settings1 is settings2
        assert settings_manager1 is settings_manager2
        assert settings_manager1 == settings_manager2

    def test_error_proxy_invalid_json(self):
        settings_manager = SettingsManager()
        settings_manager.open("json/invalid.json")

        assert type(settings_manager.error) is OperationException

    def test_error_proxy_invalid_value_of_field(self):
        settings_manager = SettingsManager()
        settings_manager.open("json/settings_invalid_field.json.json")

        assert type(settings_manager.error) is OperationException
