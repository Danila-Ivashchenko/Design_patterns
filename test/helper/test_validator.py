import unittest as un

from src.core.domain.errors.argument import ArgumentException
from src.core.util.helper.validator import Validator


class ValidatorTests(un.TestCase):
    def test_validation_type(self):
        v = Validator()
        s_var = "string"
        int_var = 1
        bool_var = False
        float_var = 1.2

        v.validate_type(s_var, str)
        v.validate_type(int_var, int)
        v.validate_type(bool_var, bool)
        v.validate_type(float_var, float)

        is_ok = False

        assert v.validate() is None

    def test_validation_type_wrong(self):
        s_var = "string"

        with self.assertRaises(ArgumentException):
            Validator().validate_type(s_var, int).validate()

    def test_validation_invalid_length(self):
        s_var = "123"

        with self.assertRaises(ArgumentException):
            Validator().validate_length(s_var, 4).validate()

    def test_validation_max_or_equal_length(self):
        Validator().validate_max_or_equal_length("222", 3).validate()

        with self.assertRaises(ArgumentException):
            Validator().validate_max_or_equal_length("123", 2).validate()

    def test_validation_max_length(self):
        Validator().validate_max_length("222", 4).validate()

        with self.assertRaises(ArgumentException):
            Validator().validate_max_length("123", 3).validate()

    def test_validation_min_length(self):
        Validator().validate_min_length("222", 2).validate()

        with self.assertRaises(ArgumentException):
            Validator().validate_min_length("123", 3).validate()

    def test_validation_min_value(self):
        Validator().validate_min_value(1, 0).validate()

        with self.assertRaises(ArgumentException):

            Validator().validate_min_value(0, 1).validate()
            Validator().validate_min_value(-1, 1).validate()

    def test_validation_multyply(self):
        s_var = "string"

        assert Validator().\
            validate_type(s_var, str).\
            validate_min_length(s_var, 3).\
            validate_max_length(s_var, 10).validate() is None

