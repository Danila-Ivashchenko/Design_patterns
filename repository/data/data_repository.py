
class DataRepository():

    __data = {}
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataRepository, cls).__new__(cls)
        return cls._instance

    @property
    def data(self):
        return self.__data

    @staticmethod
    def nomenclatura_group_key() -> str:
        return "nomenclatura_group"

    @staticmethod
    def nomenclature_key() -> str:
        return "nomenclature"

    @staticmethod
    def measurement_unit_key() -> str:
        return "measurement_unit"

    @staticmethod
    def ingredient_key() -> str:
        return "ingredient"

    @staticmethod
    def recipe_key() -> str:
        return "recipe"

    @staticmethod
    def organization_key() -> str:
        return "organization"

    