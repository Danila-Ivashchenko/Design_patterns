from enum import Enum


class EventType(Enum):
    DELETE_NOMENCLATURE = 1
    CHANGE_NOMENCLATURE = 2

    CHANGE_MEASUREMENT_UNIT = 3
    CHANGE_BLOCK_DATE = 4

    DUMP_DATA = 5

    GOT_HTTP_REQUEST = 6


