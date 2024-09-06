"""Demo context manager making a resource context-capable."""

import logging
import logging.handlers
from contextlib import contextmanager
from typing import Generator


def get_logger(name: str, stream: str | bool = 'INFO', file: str | bool = '',
               *, level: str = 'DEBUG') -> logging.Logger:
    """configure a logger with multiple handlers

    Args:
        name: the name of the logger that will be shown in the logs
        stream: set stream log level, default is 'INFO'
        file: set rotating file log level, default is OFF
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

    console_handler = logging.StreamHandler()
    if stream in LOG_LEVEL and (console_handler.__class__ not in
                                {h.__class__ for h in logger_.handlers}):
        console_handler.setLevel(LOG_LEVEL[stream])
        c_format = logging.Formatter("#%(levelname)9s - %(filename)s:%(lineno)d"
                                     " %(name)s.%(funcName)s() - %(message)s")
        console_handler.setFormatter(c_format)
        logger_.addHandler(console_handler)

    log_file = f"{__file__[:-3]}.log"
    file_handler_class = logging.handlers.RotatingFileHandler
    if file in LOG_LEVEL and (file_handler_class not in
                              {h.__class__ for h in logger_.handlers}):
        file_handler = file_handler_class(
            log_file, maxBytes=1048576, backupCount=9, encoding='utf-8')
        file_handler.setLevel(LOG_LEVEL[file])
        f_format = logging.Formatter("%(asctime)s %(levelname)s - %(module)s "
                                     "- %(filename)s:%(lineno)d  "
                                     "%(name)s.%(funcName)s() - %(message)s")
        file_handler.setFormatter(f_format)
        logger_.addHandler(file_handler)

    if not logger_.hasHandlers():
        logger_.addHandler(logging.NullHandler())

    return logger_


@contextmanager
def logging_context(*args, **kwargs) -> Generator[logging.Logger, None, None]:
    """use contextmanager to setup/shutdown logging"""
    try:
        logger_ = get_logger(*args, **kwargs)
        yield logger_
    finally:
        try:
            logger_.info("shutting down the logging facility...")
        except Exception as e:
            print(f"Can't log final message to logger, {e=}"
                  "shutting down the logging facility...")
        logging.shutdown()


def main() -> None:
    """log info, will appear both on screen and in file"""
    logger.debug("this is a DEBUG level message")
    logger.info("this is an INFO level message")
    logger.warning("this is a WARNING level message")
    logger.error("this is a ERROR level message")
    logger.critical("this is a CRITICAL level message")


if __name__ == "__main__":
    with logging_context(__name__, 'INFO', 'DEBUG') as logger:
        main()

#     INFO - m8_2_2.py:73 __main__.main() - this is an INFO level message
#  WARNING - m8_2_2.py:74 __main__.main() - this is a WARNING level message
#    ERROR - m8_2_2.py:75 __main__.main() - this is a ERROR level message
# CRITICAL - m8_2_2.py:76 __main__.main() - this is a CRITICAL level message
#     INFO - m8_2_2.py:63 __main__.logging_context() - shutting down the logging facility...
