"""Demo try-except-else-finally structure"""

from os.path import basename
import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)9s\
 - %(filename)s:%(lineno)d  %(name)s.%(funcName)s() - %(message)s")
logger = logging.getLogger(__name__)


def safe_read_file(fname: str) -> str | None:
    """open the given filename, read it's first line, and return it. 

    If run into exception, will report the error, otherwise, report
    the read is finished properly.

    Args:
        fname: string representing the file name to open.

    Returns:
        the first line of the file as a stirng.
    """
    logger.debug("trying to work with file ...%s", basename(fname))
    try:
        file = None
        file = open(fname, "r", encoding='utf-8')
        data = file.readline()
    except FileNotFoundError as e:
        logger.error(" file %s was not found, line %s",
                     basename(fname), e.__traceback__.tb_lineno)
    except Exception as e:
        logger.error("  Unexpected Exception: %r, line %s",
                     e, e.__traceback__.tb_lineno)
    else:
        logger.info(" in the else block (finished reading file properly)")
        return data.strip()
    finally:
        if file:
            file.close()
            logger.info(" in the finally block: File closed.")
        else:
            logger.info(" in the finally block, File was never opened.")

    logger.error("  !func safe_read_file ended with errors.")
    return None


def main(fnames: list[str]) -> None:
    """main func demo sending different filename to safe_read_file.

    Args:
        fnames: a list containing filename to open and read.
    """
    for fname in fnames:
        print(f"# 1st line of text in file:{safe_read_file(fname)}")


if __name__ == "__main__":
    try:
        file_names = [__file__, "donot.exist"]
        main(file_names)
    finally:
        logger.info("shutting down logging.")
        logging.shutdown()

#    DEBUG - m8_1_4.py:22  __main__.safe_read_file() - trying to work with file ...m8_1_4.py
#     INFO - m8_1_4.py:34  __main__.safe_read_file() -  in the else block (finished reading file properly)
#     INFO - m8_1_4.py:39  __main__.safe_read_file() -  in the finally block: File closed.
# 1st line of text in file:"""Demo try-except-else-finally structure"""
#    DEBUG - m8_1_4.py:22  __main__.safe_read_file() - trying to work with file ...donot.exist
#    ERROR - m8_1_4.py:28  __main__.safe_read_file() -  file donot.exist was not found, line 25
#     INFO - m8_1_4.py:41  __main__.safe_read_file() -  in the finally block, File was never opened.
#    ERROR - m8_1_4.py:43  __main__.safe_read_file() -   !func safe_read_file ended with errors.
# 1st line of text in file:None
#     INFO - m8_1_4.py:62  __main__.<module>() - shutting down logging.
