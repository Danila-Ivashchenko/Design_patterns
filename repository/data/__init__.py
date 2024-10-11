class DataRepository:
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
    def nomenclature_key() -> str:
        return "nomenclature"

    @staticmethod
    def nomenclature_group_key() -> str:
        return "nomenclature_group"

    @staticmethod
    def measurement_unit_key() -> str:
        return "measurement_unit"

    @staticmethod
    def receipt_key() -> str:
        return "recipe"

    @staticmethod
    def get_all_keys() -> list:
        return [DataRepository.nomenclature_key(), DataRepository.nomenclature_group_key(),
                DataRepository.measurement_unit_key(), DataRepository.receipt_key()]
