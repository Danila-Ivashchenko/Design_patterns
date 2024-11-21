import sys
from datetime import datetime

from src.core.util.logger.entry import LogLevel, LogEntry


class Logger:
    __log_level = LogLevel.DEBUG
    __output = sys.stdout

    @staticmethod
    def set_log_level(log_level: LogLevel):
        Logger.__log_level = log_level
        Logger.info(f"Log level set to {log_level.name}", {"location": "set_log_level"})

    @staticmethod
    def get_log_level() -> LogLevel:
        return Logger.__log_level

    @staticmethod
    def set_file_output(output):
        Logger.__output = output

    @staticmethod
    def __print(entry: LogEntry):
        if entry.level.value < Logger.__log_level.value:
            return

        time = datetime.now().isoformat()
        hooks = ""
        for hook in entry.hooks.keys():
            hook_value = f"[{hook}"
            if entry.hooks[hook] is not None:
                hook_value += f": {entry.hooks[hook]}"

            hook_value += "] "
            hooks += hook_value

        message = f"{entry.level.name}: [{time}] {hooks}\t{entry.message}"

        Logger.__output.write(f"{message}\n")
        Logger.__output.flush()

    @staticmethod
    def debug(message: str, hooks=None):
        if hooks is None:
            hooks = {}

        entry = LogEntry(LogLevel.DEBUG, message)
        entry.add_hooks(hooks)

        Logger.__print(entry)

    @staticmethod
    def info(message: str, hooks=None):
        if hooks is None:
            hooks = {}

        entry = LogEntry(LogLevel.INFO, message)
        entry.add_hooks(hooks)

        Logger.__print(entry)

    @staticmethod
    def error(message: str, hooks=None):
        if hooks is None:
            hooks = {}

        entry = LogEntry(LogLevel.ERROR, message)
        entry.add_hooks(hooks)

        Logger.__print(entry)