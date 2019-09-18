import logging
from logging import FileHandler
from logging import Formatter

# формат логов
LOG_FORMAT_FILE = (
    "%(asctime)s [%(levelname)s]: %(message)s")

LOG_FORMAT_STREAM = (
    "%(name)s - %(levelname)s - %(message)s")

# тип логов
LOG_LEVEL = logging.INFO

# наименование файла логов
LOG_FILE = "file.log"

logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)

# пишем логи в файл file.log
logger_file_handler = FileHandler(LOG_FILE)
logger_file_handler.setLevel(LOG_LEVEL)
logger_file_handler.setFormatter(Formatter(LOG_FORMAT_FILE))
logger.addHandler(logger_file_handler)

logger_stream_handler = logging.StreamHandler()
logger_stream_handler.setLevel(LOG_LEVEL)
logger_stream_handler.setFormatter(Formatter(LOG_FORMAT_STREAM))
logger.addHandler(logger_stream_handler)
