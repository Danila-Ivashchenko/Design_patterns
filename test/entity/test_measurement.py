import unittest as un
import entity
import errors


class ValidationMeasurementTests(un.TestCase):
    def test_measure_unit_fields(self):
        gram = entity.MeasurementUnit("грам", 1.0)

        assert gram.ratio == 1
        assert gram.name == "грам"
        assert gram.parent_unit == None

    def test_measure_unit_fields_validation(self):
        gram = entity.MeasurementUnit("грам", 1.0)

        assert gram.ratio == 1
        assert gram.name == "грам"
        assert gram.parent_unit == None

        with self.assertRaises(errors.ArgumentException):
            kilogram = entity.MeasurementUnit("килограм", 1, gram)


    def test_parent_unit(self):
        gram = entity.MeasurementUnit("грам", 1.0)
        kilogram = entity.MeasurementUnit("килограмм", 1000.0, gram)

        assert kilogram.parent_unit == gram
        assert kilogram.parent_unit == gram

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


