"""main module demo file operations"""

import logging
logging.basicConfig(level=logging.INFO, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

def main(file_name: str) -> None:
    """Main func demo file creation, open for read and close.

    Will first open file_name for write, create if not yet exist, 
    truncate the file if already exist. Then close it.
    Next, open file_name for read. Then close it.
    Will print out file type and closed state.
    
    Args:
        file_name: string representing file name to create and open.

    Returns: 
        None
    """
    file_w = open(file_name,'w', encoding='utf-8')
    logger.info(f"{type(file_w)=}, {file_w.closed=}")
    
    file_w.close()
    logger.info(f"{type(file_w)=}, {file_w.closed=}")
    
    file_rb = open(file_name, 'r+b')
    logger.info(f"{type(file_rb)=}, {file_rb.closed=}")
    
    file_rb.close()
    logger.info(f"{type(file_rb)=}, {file_rb.closed=}")

if __name__ == "__main__":
    base_name = __file__[:-3]
    file_name = base_name + ".data"
    main(file_name)

#INFO - __main__(m7_1.py:23) - type(file_w)=<class '_io.TextIOWrapper'>, file_w.closed=False
#INFO - __main__(m7_1.py:26) - type(file_w)=<class '_io.TextIOWrapper'>, file_w.closed=True
#INFO - __main__(m7_1.py:29) - type(file_rb)=<class '_io.BufferedRandom'>, file_rb.closed=False
#INFO - __main__(m7_1.py:32) - type(file_rb)=<class '_io.BufferedRandom'>, file_rb.closed=True
