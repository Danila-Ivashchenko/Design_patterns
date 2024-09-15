from errors.base import  AbstractException


class OperationException(AbstractException):

    @classmethod
    def fail_to_parce_json(cls, exception):
        return OperationException(f"fail to parce json: {exception}")

