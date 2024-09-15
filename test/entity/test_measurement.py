import unittest as un
import entity


class ValidationErrorTests(un.TestCase):
    def test_measure_unit_fields(self):
        gram = entity.MeasurementUnit("грам", 1.0)

        assert gram.ratio == 1
        assert gram.name == "грам"
        assert gram.parent_unit is None

    def test_parent_unit(self):
        gram = entity.MeasurementUnit("грам", 1.0)
        kilogram = entity.MeasurementUnit("килограмм", 1000.0, gram)

        assert kilogram.parent_unit == gram
        assert kilogram.parent_unit is gram

    def test_eq_false(self):
        gram = entity.MeasurementUnit("грам", 1.0)
        kilogram = entity.MeasurementUnit("килограмм", 1000.0, gram)

        assert not kilogram == gram

    def test_eq_true(self):
        sm = entity.MeasurementUnit("сантиметр", 1.0)
        m = entity.MeasurementUnit("метр", 100.0, sm)
        dm = entity.MeasurementUnit("дециметр", 10.0, sm)
        dm_x10 = entity.MeasurementUnit("дециметр * 10", 10.0, dm)

        assert dm_x10 == m


