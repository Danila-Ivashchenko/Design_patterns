from src.core.domain.errors import AbstractException


class NotFoundException(AbstractException):
    def __init__(self, message: str):
        super().__init__(message, 404, True)

    @classmethod
    def not_found_measurement_unit(cls, id: str):
        return cls(f"measurement unit not found by id: {id}")

    @classmethod
    def not_found_entity_by_id(cls, entity: str, id: str):
        return cls(f"{entity} not found by id: {id}")