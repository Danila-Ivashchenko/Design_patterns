from abc import abstractmethod

from src.core.util.helper.json import JsonHelper
from src.core.util.helper.validator import Validator


class BaseRepository:

    _validator: Validator
    _json_helper: JsonHelper

    def __init__(self):
        self._validator = Validator()
        self._json_helper = JsonHelper()

    @abstractmethod
    def dump_json(self):
        pass