from src.core.domain.errors.abstract import  AbstractException


class OperationException(AbstractException):

    @classmethod
    def fail_to_parce_json(cls, exception):
        return OperationException(f"fail to parce json: {exception}", 500, True)

    @classmethod
    def empty_data_path(cls):
        return OperationException(f"empty data path", 500, True)

    @classmethod
    def operation_doesnt_set(cls, operation):
        return OperationException(f'operation doesnt set: {operation}')

