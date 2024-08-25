"""Demonstrate logging handler and log to multiple destinations

Usage:
    python -m m7_4_4_II
"""

import logging
import logging.handlers
namebase = __file__[:-3]
log_file = f"{namebase}.log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
c_format = logging.Formatter("#%(levelname)9s - %(filename)s:%(lineno)d"
                             " %(name)s.%(funcName)s() - %(message)s")
console_handler.setFormatter(c_format)
logger.addHandler(console_handler)

file_handler = logging.handlers.RotatingFileHandler(
    log_file, maxBytes=1048576, backupCount=9, encoding='utf-8')
f_format = logging.Formatter("%(asctime)s %(levelname)s - %(module)s - "
                             "%(filename)s:%(lineno)d  %(name)s.%(funcName)s()"
                             " - %(message)s")
file_handler.setFormatter(f_format)
logger.addHandler(file_handler)


def main():
    """log info, will appear both on screen and in file"""
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

#     INFO - m7_4_4_II.py:41 __main__.<module>() - log set to /workspaces/python-book/m7_4_4_II.log, calling main()
#     INFO - m7_4_4_II.py:34 __main__.main() - this is an INFO level message
#  WARNING - m7_4_4_II.py:35 __main__.main() - this is a WARNING level message
#    ERROR - m7_4_4_II.py:36 __main__.main() - this is a ERROR level message
# CRITICAL - m7_4_4_II.py:37 __main__.main() - this is a CRITICAL level message
#     INFO - m7_4_4_II.py:43 __main__.<module>() - returned from  main()
