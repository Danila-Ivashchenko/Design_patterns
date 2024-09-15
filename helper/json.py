from copy import deepcopy
from helper.validator import Validator
def parse_fields(obj):
    return list(filter(lambda x: not x.startswith("_"), dir(obj)))

def from_json(data, class_of_obj):
    Validator().validate_type(class_of_obj, type).validate()
    fields = parse_fields(class_of_obj)

    new_obj = class_of_obj()

    data_keys = data.keys()

    for field in fields:
        if field in data_keys:
            setattr(new_obj, field, data[field])

    return new_obj