from manager import SettingsManager


def test_is_singleton():
    settings_manager1 = SettingsManager()
    settings_manager1.open("json/settings_1.json")

    settings_manager2 = SettingsManager()
    settings_manager2.open("json/settings_2.json")

    settings1 = settings_manager1.settings
    settings2 = settings_manager2.settings

    assert settings1 is settings2
    assert settings_manager1 is settings_manager2
    assert settings_manager1 == settings_manager2

