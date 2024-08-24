"""Demo context manager making a resource context-capable."""

import logging
import logging.handlers
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def logging_context(name: str, stream: str = 'INFO', file: str = '', *,
                    level: str = 'DEBUG') -> Iterator[logging.Logger]:
    """using contextmanager to setup/shutdown logging

    Args:
        name: the name of the logger that will be shown in the logs
        stream: if Truthy set stream log level to it, default is INFO
        file: if Truthy set rotating file log level to it, default is ''
        level: the logger's own level, default is 'DEBUG'

    Yields:
        logger: the logger object with name and handler set up
    """
    LOG_LEVEL = {
        "INFO": logging.INFO,
        "DEBUG": logging.DEBUG,
        "ERROR": logging.ERROR,
        "WARNING": logging.WARNING,
        "CRITICAL": logging.CRITICAL
    }
    logger_ = logging.getLogger(name)
    logger_.setLevel(LOG_LEVEL[level] if level in LOG_LEVEL else logging.DEBUG)

    if stream in LOG_LEVEL:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(LOG_LEVEL[stream])
        c_format = logging.Formatter("#%(levelname)s - %(name)s(%(filename)s:"
                                     "%(lineno)d) - %(message)s")
        console_handler.setFormatter(c_format)
        logger_.addHandler(console_handler)

    if file in LOG_LEVEL:
        log_file = f"{__file__[:-3]}.log"
        file_handler = logging.handlers.RotatingFileHandler(
            log_file, maxBytes=1048576, backupCount=9, encoding='utf-8')
        file_handler.setLevel(LOG_LEVEL[file])
        f_format = logging.Formatter("%(asctime)s %(levelname)s - %(name)s "
                                     "%(module)s.%(funcName)s:%(lineno)d - "
                                     "%(message)s")
        file_handler.setFormatter(f_format)
        logger_.addHandler(file_handler)

    try:
        yield logger_
    finally:
        logging.shutdown()


def main():
    """log info, will appear both on screen and in file"""
    logger.debug("this is a DEBUG level message")
    logger.info("this is an INFO level message")
    logger.warning("this is a WARNING level message")
    logger.error("this is a ERROR level message")
    logger.critical("this is a CRITICAL level message")


if __name__ == "__main__":
    with logging_context(__name__, file='DEBUG') as logger:
        main()

#INFO - __main__(m8_2_2.py:38) - this is an INFO level message
#WARNING - __main__(m8_2_2.py:39) - this is a WARNING level message
#ERROR - __main__(m8_2_2.py:40) - this is a ERROR level message
#CRITICAL - __main__(m8_2_2.py:41) - this is a CRITICAL level message
