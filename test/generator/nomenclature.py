from entity import Nomenclature
from generator import NomenclatureGenerator, MeasurementUnitGenerator
import unittest as un


class NomenclatureGeneratorTests(un.TestCase):

    def test_creating(self):
        gen = NomenclatureGenerator()
        mes_unit_gen = MeasurementUnitGenerator()

        oil = gen.oil
        assert oil.name == "масло"
        assert oil.measurement_uint == mes_unit_gen.milliliter

        salt = gen.salt
        assert salt.name == "соль"
        assert salt.measurement_uint == mes_unit_gen.gram

        milk = gen.milk
        assert milk.name == "молоко"
        assert milk.measurement_uint == mes_unit_gen.milliliter

        chicken_fillet = gen.chicken_fillet
        assert chicken_fillet.name == "куриное филе"
        assert chicken_fillet.measurement_uint == mes_unit_gen.gram