""" Demonstrating log to file.

Usage:
    python -m m7_4_4_I
"""
import os
import logging
namebase = __file__[:-3]
log_file = f"{namebase}.log"
if os.path.exists(log_file):
    os.replace(log_file, f"{log_file}.old")
logging.basicConfig(filename=log_file, filemode='w',
                    level=logging.DEBUG, format="%(asctime)s %(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)


def main():
    """log different level of messages to log file"""
    logger.debug("this is a DEBUG level message")
    logger.info("this is an INFO level message")
    logger.warning("this is a WARNING level message")
    logger.error("this is a ERROR level message")
    logger.critical("this is a CRITICAL level message")


if __name__ == '__main__':
    logger.info("log set to %s, calling main()", log_file)
    main()
    logger.info("returned from  main()")
    logging.shutdown()
