import os

from manager import SettingsManager



def test_load_settings_from_json():
    settings_manager = SettingsManager()
    settings_manager.open("json/settings_1.json")

    settings = settings_manager.settings
    assert settings.inn == "180080920202"
    assert settings.account == "10702810203"
    assert settings.correspondent_account == "10702810204"
    assert settings.bik == "144030001"
    assert settings.ownership_type == "12345"
    assert settings.organization_name == "Roga and kopyta TEST"
    assert settings.director_name == "Danila Ivaschenko TEST"


def test_load_settings_from_invalid_json():
    settings_manager = SettingsManager()
    settings_manager.open("json/invalid.json")

    settings = settings_manager.settings
    assert settings.inn == "380080920202"
    assert settings.account == "40702810203"
    assert settings.correspondent_account == "40702810204"
    assert settings.bik == "044030001"
    assert settings.ownership_type == "общая"
    assert settings.organization_name == "Рога и копыта (default)"
    assert settings.director_name == "Директор (default)"