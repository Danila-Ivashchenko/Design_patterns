from src.core.domain.errors import AbstractException


class IsUsedException(AbstractException):
    def __init__(self, message: str):
        super().__init__(message, 400, True)

    @classmethod
    def used_entity_by_id(cls, entity: str, id: str):
        return cls(f"used {entity} with id: {id}")