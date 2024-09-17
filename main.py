from manager import SettingsManager


m = SettingsManager()

m.open()
print(m.error)
print(m.settings)