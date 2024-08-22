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
    file_w = open(file_name, 'w', encoding='utf-8')
    logger.info("Text file is opened for write as %s, %s",
                type(file_w), f"{file_w.closed=}")

    file_w.close()
    logger.info("File is still %s, %s", type(file_w), f"{file_w.closed=}")

    file_rb = open(file_name, 'r+b')
    logger.info("Binary file is opened for read as %s, %s",
                type(file_rb), f"{file_w.closed=}")

    file_rb.close()
    logger.info("File is still %s, %s", type(file_rb), f"{file_w.closed=}")


if __name__ == "__main__":
    namebase = __file__[:-3]
    filename = namebase + ".data"
    main(filename)

#INFO - __main__(m7_1.py:24) - Text file is opened for write as <class '_io.TextIOWrapper'>, file_w.closed=False
#INFO - __main__(m7_1.py:28) - File is still <class '_io.TextIOWrapper'>, file_w.closed=True
#INFO - __main__(m7_1.py:31) - Binary file is opened for read as <class '_io.BufferedRandom'>, file_w.closed=True
#INFO - __main__(m7_1.py:35) - File is still <class '_io.BufferedRandom'>, file_w.closed=True
