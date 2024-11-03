from src.core.util.helper.validator import Validator


class BaseDTO:
    _validator: Validator

    def __init__(self):
        self._validator = Validator()