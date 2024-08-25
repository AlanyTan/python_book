"""Demo nested try-except structure"""

from os.path import basename
import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)9s\
 - %(filename)s:%(lineno)d  %(name)s.%(funcName)s() - %(message)s")
logger = logging.getLogger(__name__)


def safe_read_file(fname: str, size: int) -> str | None:
    """open the given filename, read it's first line, and return it. 

    It tries to open the given filename, and read the first line, 
    if run into exception, will report the error, otherwise, report
    the read is finished properly. 
    If run into exceptions during closing of the file, it reports 
    the closing error, and ask if the file was ever open.

    Args:
        fname: string representing the file name to open.

    Returns:
        the first line of the file as a stirng.
    """
    logger.debug("trying to work with file ...%s", basename(fname))
    try:
        try:
            file = open(fname, "r", encoding='utf-8')
        except FileNotFoundError as e:
            logger.warning(" in inner except, file not found line %s, "
                           "trying adding current filename as prefix.",
                           e.__traceback__.tb_lineno)
            file = open(__file__[:-2] + fname, "r", encoding='utf-8')
    except FileNotFoundError as e:
        logger.error(" in exept block, the file %s was not found, line %s",
                     basename(fname), e.__traceback__.tb_lineno)
    except Exception as e:
        logger.error("unexpected error %r, line %s",
                     e, e.__traceback__.tb_lineno)
    else:
        logger.debug(" in else block opened file successfully.")
        try:
            data = file.read(size)
        except TypeError as e:
            logger.warning("reading %r chars from %s failed with %r, line %s, "
                           "reading the first line instead",
                           size, basename(fname), e, e.__traceback__.tb_lineno)
            data = file.readline().strip()
            logger.info("read first line from the file instead (%s chars)",
                        len(data))
        except Exception as e:
            logger.error("unexpected error %r, line %s",
                         e, e.__traceback__.tb_lineno)
            data = None
        else:
            logger.info("successfully read %s chars from %s",
                        size, basename(fname))

        return data
    finally:
        try:
            file.close()
            logger.debug(" in finally block: File closed.")
        except Exception as e:
            logger.warning(" closing %s run into exception: %r, "
                           "maybe it was never opened?",
                           basename(fname), e)
    return None


def main(fname: str) -> None:
    """main func demo sending different denominators to save_divide.

    Args:
        list_of_numbers_to_try: a list containing numbers to be used
        as denominator when trying to call save_divide.
    """
    print(f"# first 16 chars of file:{safe_read_file(fname, 16)}")
    print(f"# first 16 chars of file fallback:{safe_read_file("py", 16)}")
    print(f"# wrong type of size in file:{safe_read_file(fname, 'sixteen')}")
    print(f"# non-exist file:{safe_read_file('donot.exist', 0)}")


if __name__ == "__main__":
    try:
        file_name = __file__
        main(file_name)
    finally:
        logger.info("shutting down logging.")
        logging.shutdown()

#    DEBUG - m8_1_5.py:25  __main__.safe_read_file() - trying to work with file ...m8_1_5.py
#    DEBUG - m8_1_5.py:41  __main__.safe_read_file() -  in else block opened file successfully.
#     INFO - m8_1_5.py:56  __main__.safe_read_file() - successfully read 16 chars from m8_1_5.py
#    DEBUG - m8_1_5.py:63  __main__.safe_read_file() -  in finally block: File closed.
# first 16 chars of file:"""Demo nested t
#    DEBUG - m8_1_5.py:25  __main__.safe_read_file() - trying to work with file ...py
#  WARNING - m8_1_5.py:30  __main__.safe_read_file() -  in inner except, file not found line 28, trying adding current filename as prefix.
#    DEBUG - m8_1_5.py:41  __main__.safe_read_file() -  in else block opened file successfully.
#     INFO - m8_1_5.py:56  __main__.safe_read_file() - successfully read 16 chars from py
#    DEBUG - m8_1_5.py:63  __main__.safe_read_file() -  in finally block: File closed.
# first 16 chars of file fallback:"""Demo nested t
#    DEBUG - m8_1_5.py:25  __main__.safe_read_file() - trying to work with file ...m8_1_5.py
#    DEBUG - m8_1_5.py:41  __main__.safe_read_file() -  in else block opened file successfully.
#  WARNING - m8_1_5.py:45  __main__.safe_read_file() - reading 'sixteen' chars from m8_1_5.py failed with TypeError("argument should be integer or None, not 'str'"), line 43, reading the first line instead
#     INFO - m8_1_5.py:49  __main__.safe_read_file() - read first line from the file instead (38 chars)
#    DEBUG - m8_1_5.py:63  __main__.safe_read_file() -  in finally block: File closed.
# wrong type of size in file:"""Demo nested try-except structure"""
#    DEBUG - m8_1_5.py:25  __main__.safe_read_file() - trying to work with file ...donot.exist
#  WARNING - m8_1_5.py:30  __main__.safe_read_file() -  in inner except, file not found line 28, trying adding current filename as prefix.
#    ERROR - m8_1_5.py:35  __main__.safe_read_file() -  in exept block, the file donot.exist was not found, line 33
#  WARNING - m8_1_5.py:65  __main__.safe_read_file() -  closing donot.exist run into exception: UnboundLocalError("cannot access local variable 'file' where it is not associated with a value"), maybe it was never opened?
# non-exist file:None
#     INFO - m8_1_5.py:89  __main__.<module>() - shutting down logging.
