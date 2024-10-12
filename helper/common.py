import datetime

from abstract import TypedNone, TypedList

class CommonParser:

    __ignored_fields = ["validator"]
    __primitive_types = (str, int, float, bool, TypedNone, TypedList, list, dict, datetime.datetime)

    def parse_fields(self, obj):
        if isinstance(obj, self.__primitive_types):
            return []
        if obj is None:
            return []
        return list(filter(lambda x: not x.startswith("_") and x not in self.__ignored_fields and not callable(getattr(obj.__class__, x)), dir(obj)))
