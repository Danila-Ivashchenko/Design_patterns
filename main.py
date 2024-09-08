from manager import SettingsManager

manager1 = SettingsManager()
manager1.open("json/settings_2.json")

manager = SettingsManager()
manager.open("json/settings_2.json")

settings1 = manager1.settings
settings = manager.settings

print(settings1)
print(settings)

settings1.validate()
