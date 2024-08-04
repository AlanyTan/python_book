import os
base_name = __file__[:-3]
log_file = f"{base_name}.log"

import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
c_format = logging.Formatter("#%(levelname)s - "
                             "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
console_handler.setFormatter(c_format)
logger.addHandler(console_handler)

file_handler = logging.handlers.RotatingFileHandler(
    log_file, maxBytes=1048576, backupCount=9, encoding='utf-8')
f_format = logging.Formatter("%(asctime)s %(levelname)s - %(name)s "
                "%(module)s.%(funcName)s:%(lineno)d - %(message)s")
file_handler.setFormatter(f_format)
logger.addHandler(file_handler)


def main(base_name: str):
    logger.debug(f"this is a DEBUG level message")
    logger.info(f"this is an INFO level message")
    logger.warning(f"this is a WARNING level message")
    logger.error(f"this is a ERROR level message")
    logger.critical(f"this is a CRITICAL level message")
    
if __name__ == '__main__':
    base_name = __file__[:-3]
    logger.info(f"log set to {os.path.basename(base_name)}.log, calling main()")
    main(base_name)
    logging.shutdown()
    
#INFO - __main__(m7_4_4_II.py:35) - log file set to m7_4_4_II.log, calling main
#INFO - __main__(m7_4_4_II.py:28) - this is an INFO level message
#WARNING - __main__(m7_4_4_II.py:29) - this is a WARNING level message
#ERROR - __main__(m7_4_4_II.py:30) - this is a ERROR level message
#CRITICAL - __main__(m7_4_4_II.py:31) - this is a CRITICAL level message
