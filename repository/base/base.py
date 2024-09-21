from helper import Validator


class BaseRepository:

    _validator: Validator

    def __init__(self):
        self._validator = Validator()