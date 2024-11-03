import datetime


class UpdateDateBlockDTO:
    __value: datetime.datetime = None

    @property
    def value(self) -> datetime.datetime:
        return self.__value

    @value.setter
    def value(self, value: datetime.datetime | int):
        if isinstance(value, int):
            value = datetime.datetime.fromtimestamp(value)
        self.__value = value