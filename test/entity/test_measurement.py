import unittest as un

from src.core.domain.entity.measurement_unit import MeasurementUnit
from src.core.domain.errors.argument import ArgumentException


class ValidationMeasurementTests(un.TestCase):
    def test_measure_unit_fields(self):
        gram = MeasurementUnit("грам", 1.0)

        assert gram.ratio == 1
        assert gram.name == "грам"
        assert gram.parent_unit == None

    def test_measure_unit_fields_validation(self):
        gram = MeasurementUnit("грам", 1.0)

        assert gram.ratio == 1
        assert gram.name == "грам"
        assert gram.parent_unit == None

        with self.assertRaises(ArgumentException):
            kilogram = MeasurementUnit("килограм", 1, gram)


    def test_parent_unit(self):
        gram = MeasurementUnit("грам", 1.0)
        kilogram = MeasurementUnit("килограмм", 1000.0, gram)

        assert kilogram.parent_unit == gram
        assert kilogram.parent_unit == gram

    def test_eq_false(self):
        gram = MeasurementUnit("грам", 1.0)
        kilogram = MeasurementUnit("килограмм", 1000.0, gram)

        assert not kilogram == gram

    def test_eq_true(self):
        sm = MeasurementUnit("сантиметр", 1.0)
        m = MeasurementUnit("метр", 100.0, sm)
        dm = MeasurementUnit("дециметр", 10.0, sm)
        dm_x10 = MeasurementUnit("дециметр * 10", 10.0, dm)

        assert dm_x10 == m


