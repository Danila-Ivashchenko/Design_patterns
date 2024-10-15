
def invalid_length(given, must_be):
    return ValueError(f"invalid length, given: {given}, must_be: {must_be}")

def value_does_not_set(value):
    return ValueError(f"value does not set: {value}")

def mast_be_bigger_zero(value):
    return ValueError(f"value must be bigger zero, given: {value}")