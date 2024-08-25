"""Demo with structure inside try-except."""

from os.path import basename
import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)9s\
 - %(filename)s:%(lineno)d  %(name)s.%(funcName)s() - %(message)s")
logger = logging.getLogger(__name__)


def safe_read_file(fname: str) -> str | None:
    """open the given filename, read it's first line and return it.

    It tries to open the given filename, and read the first line
    if run into exceptions, will report the error, otherwise report
    the read is finished. With will not try to close the file if open
    failed, so there will not be print message asking user if the file
    has ever been opened.

    Args:
        fname: string representing the file name to open.

    Returns:
        the first line of the file as string.
    """
    try:
        logger.debug("trying to work with ...%s", basename(fname))
        with open(fname, "r", encoding='utf-8') as file:
            logger.debug(" file opened as %s", type(file))
            data = file.readline()
            texts = data.strip()
        logger.debug("finished with block, file closed: %s", file.closed)
        return texts
    except FileNotFoundError as e:
        logger.error("File %s was not found, object file exist:%s, line %s",
                     basename(fname), 'file' in dir(),
                     e.__traceback__.tb_lineno)
    except Exception as e:
        logger.error("An unexpected error occurred: %r line %s",
                     e, e.__traceback__.tb_lineno)


def main(fnames: list[str]) -> None:
    """main func demo sending different denominators to save_divide.

    Args:
        fname: a list of str representing filenames to open
    """
    for fname in fnames:
        print(f"# 1st line of text in file:{safe_read_file(fname)}")


if __name__ == "__main__":
    file_names = [__file__, "example.txt"]
    main(file_names)

#    DEBUG - m8_2_1.py:26  __main__.safe_read_file() - trying to work with ...m8_2_1.py
#    DEBUG - m8_2_1.py:28  __main__.safe_read_file() -  file opened as <class '_io.TextIOWrapper'>
#    DEBUG - m8_2_1.py:31  __main__.safe_read_file() - finished with block, file closed: True
#1 st line of text in file:"""Demo with structure inside try-except."""
#    DEBUG - m8_2_1.py:26  __main__.safe_read_file() - trying to work with ...example.txt
#    ERROR - m8_2_1.py:34  __main__.safe_read_file() - File example.txt was not found, object file exist:False, line 27
# 1st line of text in file:None
