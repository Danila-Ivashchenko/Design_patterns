from copy import deepcopy
from .common import parse_fields


def from_json(data, class_obj):
    fields = parse_fields(class_obj)

    new_obj = deepcopy(class_obj)

    data_keys = data.keys()

    for field in fields:
        if field in data_keys:
            setattr(new_obj, field, data[field])

    return new_obj