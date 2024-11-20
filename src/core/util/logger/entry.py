from enum import Enum


class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    ERROR = 3


class LogEntry:
    __level: LogLevel
    __message: str
    __hooks: {}

    def __init__(self, level: LogLevel, message: str):
        self.__level = level
        self.__message = message
        self.__hooks = {}

    @property
    def level(self):
        return self.__level

    @property
    def message(self):
        return self.__message

    @property
    def hooks(self) -> dict:
        return self.__hooks

    def add_hooks(self, hooks: {}) -> 'LogEntry':
        for name, value in hooks.items():
            self.__hooks[name] = value

        return self

    def add_hook(self, name: str, value) -> 'LogEntry':
        self.__hooks[name] = value

        return self