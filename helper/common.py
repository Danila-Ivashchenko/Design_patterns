def parse_fields(obj):
    return list(filter(lambda x: not x.startswith("_"), dir(obj)))