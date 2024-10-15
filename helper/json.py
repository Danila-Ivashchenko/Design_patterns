import datetime
from copy import deepcopy
from .common import CommonParser
from abstract import TypedList, TypedNone
from helper.validator import Validator
from enum import Enum


class JsonHelper:

    __common_parser = CommonParser()
    def parse_fields(self, obj):
        return list(filter(lambda x: not x.startswith("_"), dir(obj)))

    def from_json(self, data, class_of_obj):
        Validator().validate_type(class_of_obj, type).validate()
        fields = self.parse_fields(class_of_obj)

        new_obj = class_of_obj()

        data_keys = data.keys()

        for field in fields:
            if field in data_keys:
                setattr(new_obj, field, data[field])

        return new_obj

    def to_deserialize(self, class_of_obj, data):
        if isinstance(class_of_obj, TypedList):
            item_type = class_of_obj.elem_type
            return [self.to_deserialize(item_type, data_item) for data_item in data]

        if isinstance(class_of_obj, TypedNone):
            class_of_obj = class_of_obj.elem_type

        if class_of_obj is None:
            return None

        # Validator().validate_type(class_of_obj, type).validate()
        fields = self.parse_full_field(class_of_obj)

        new_obj = class_of_obj()

        if isinstance(data, (int, float, str)):
            return data

        data_keys = data.keys()

        for field in fields:
            if field in data_keys:
                attr_val = data[field]
                if isinstance(attr_val, str) and attr_val == 'None' or attr_val == None:
                    attr_val = None
                elif isinstance(attr_val, dict):
                    attr_in_obj_val = getattr(new_obj, field)
                    if isinstance(attr_in_obj_val, (TypedNone, TypedList)):
                        attr_val = self.to_deserialize(attr_in_obj_val, attr_val)
                    else:
                        attr_val = self.to_deserialize(type(attr_in_obj_val), attr_val)

                elif isinstance(attr_val, list):
                    obj_val = getattr(new_obj, field)
                    new_items = []
                    if isinstance(obj_val, TypedList):
                        elem_type = obj_val.elem_type

                        for attr_item in attr_val:
                            new_items.append(self.to_deserialize(elem_type, attr_item))
                    else:
                        for attr_item in attr_val:
                            new_items.append(attr_item)

                    attr_val = new_items

                setattr(new_obj, field, attr_val)

        return new_obj

    def parse_full_field(self, obj):
        fileds = self.parse_fields(obj)

        if hasattr(fileds, '__dict__'):
            return [self.parse_full_field(f) for f in obj.intems()]
        elif isinstance(obj, list):
            return [self.parse_full_field(f) for f in obj]
        return fileds

    def to_serialize(self, val):
        if val == None:
            return None
        if isinstance(val, Enum):
            return val.value
        if isinstance(val, dict):
            return {str(k): self.to_serialize(v) for k, v in val.items()}
        elif isinstance(val, list):
            result = []
            for v in val:
                data = self.to_serialize(v)
                result.append(data)
            return result
            # return [self.to_serialize(v) for v in val]
        elif hasattr(val, '__dict__'):
            fields = self.__common_parser.parse_fields(val)
            return {field: self.to_serialize(getattr(val, field)) for field in fields if not callable(getattr(val, field))}
        elif isinstance(val, (int, float, bool)):
            return val
        elif isinstance(val, datetime.datetime):
            return val.timestamp()
        elif hasattr(val, '__str__'):
            return str(val)
        else:
            return val

