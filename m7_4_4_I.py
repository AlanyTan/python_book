import os
base_name = __file__[:-3]
log_file = f"{base_name}.log"
if os.path.exists(log_file):
    os.replace(log_file, f"{log_file}.old")

import logging
logging.basicConfig(filename=log_file, filemode='w',
                    level=logging.DEBUG, format="%(asctime)s %(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

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
