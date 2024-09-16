

class AbstractException(Exception):

    __message = ""

    def __init__(self, message: str):
        self.__message = message

    @property
    def message(self):
        return self.message

    @message.setter
    def message(self, message: str):
        self.__message = message



