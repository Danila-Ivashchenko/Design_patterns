from generator import MeasurementUnitGenerator
import unittest as un


class MeasurementUnitGeneratorTests(un.TestCase):

    def test_creating(self):
        gen = MeasurementUnitGenerator()

        unit = gen.thing
        assert unit.name == "штука"

        unit = gen.milliliter
        assert unit.name == "миллилитр"


        unit = gen.gram
        assert unit.name == "грамм"
        unit = gen.kilo_gram
        assert unit.name == "килограм"

        unit = gen.teaspoon
        assert unit.name == "чайная ложка"
        unit = gen.tablespoon
        assert unit.name == "столовая ложка"