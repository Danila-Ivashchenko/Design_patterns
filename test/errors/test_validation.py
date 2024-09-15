from errors.validation import ArgumentException
import unittest as un


class ValidationErrorTests(un.TestCase):
    def test_invalid_type(self):
        ex = ArgumentException.invalid_type(str, int)

        with self.assertRaises(ArgumentException):
            raise ex
