

class CommonParser:

    __ignored_fields = ["validator"]

    def parse_fields(self, obj):
        if obj is None:
            return []
        return list(filter(lambda x: not x.startswith("_") and x not in self.__ignored_fields  and not callable(getattr(obj.__class__, x)), dir(obj)))
