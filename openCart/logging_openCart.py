import logging
from logging import FileHandler
from logging import Formatter

import psycopg2

# формат логов
LOG_FORMAT_FILE = (
    "%(asctime)s [%(levelname)s]: %(message)s")

LOG_FORMAT_STREAM = (
    "%(name)s - %(levelname)s - %(message)s")

LOG_FORMAT_DB = (
    "CURRENT_TIMESTAMP, '%(level)s',  '%(message)s'")

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

# пишем логи в консоль
logger_stream_handler = logging.StreamHandler()
logger_stream_handler.setLevel(LOG_LEVEL)
logger_stream_handler.setFormatter(Formatter(LOG_FORMAT_STREAM))
logger.addHandler(logger_stream_handler)


# пишем логи в базу

class DbHandler(logging.Handler):
    """
    A handler class which writes formatted logging records to db
    """

    def __init__(self):
        """
        Open the specified file and use it as the stream for logging.
        """
        logging.Handler.__init__(self)
        self.connection = None
        self.cursor = None
        self.connect_database()

    def close(self):
        """
        Closes the stream.
        """
        self.acquire()
        try:
            try:
                self.cursor.close()
            finally:
                pass
            try:
                self.connection.close()
            finally:
                pass
            logging.Handler.close(self)
        finally:
            self.release()

    def connect_database(self):
        self.connection = psycopg2.connect(user="postgres",
                                           password="postgres",
                                           host="127.0.0.1",
                                           port="5432",
                                           database="testlog")
        self.cursor = self.connection.cursor()
        pass

    def emit(self, record):
        """
        Emit a record.

        If the stream was not opened because 'delay' was specified in the
        constructor, open it before calling the superclass's emit.
        """
        sql = 'INSERT INTO main.logs (datetime, type, logs) VALUES (' + LOG_FORMAT_DB + ')'
        message_ = sql % {'level': record.levelname, 'message': record.message.replace("'", "''")}
        self.cursor.execute(message_)
        self.connection.commit()

    def __repr__(self):
        level = logging.getLevelName(self.level)
        return '<%s (%s)>' % (self.__class__.__name__, level)


logger_db_handler = DbHandler()
logger_db_handler.setLevel(LOG_LEVEL)
logger_db_handler.setFormatter(Formatter(LOG_FORMAT_DB))
logger.addHandler(logger_db_handler)
