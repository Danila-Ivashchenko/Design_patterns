
import unittest as un

from src.core.domain.errors.argument import ArgumentException


class ValidationErrorTests(un.TestCase):
    def test_invalid_type(self):
        ex = ArgumentException.invalid_type(str, int)

        with self.assertRaises(ArgumentException):
            raise ex
