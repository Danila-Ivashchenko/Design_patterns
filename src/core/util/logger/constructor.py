import sys

from src.core.domain.entity.settings import Settings
from src.core.util.logger.logger import Logger


def setup_logger(settings: Settings):
    log_level = settings.log_level
    log_file_path = settings.log_file
    log_output = sys.stdout

    if log_file_path != "":
        log_output = open(log_file_path, "a")

    Logger.set_log_level(log_level)
    Logger.set_file_output(log_output)