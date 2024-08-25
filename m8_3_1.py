"""Demo raise..., raise ... from e, and raise.

Usage:
    python m8_3_1.py
"""

from os.path import basename
import traceback
from m8_2_2 import logging_context as log_to


def safe_read_file(fname: str, size: int) -> str | None:
    """open the given filename, read it's first line, and return it. 

    It tries to open the given filename, and read the first size of characters, 
    if fname is not found, it tries to treat fname as extention name and try
    to add current program filename trunk as prefix; if size is not numerical
    it tries to read the first line instead.

    Args:
        fname: string representing the file name to open.
        size: number of characters to read and return.

    Returns:
        the first line of the file as a stirng.
    """
    logger.debug("trying to work with file ...%s", basename(fname))
    try:
        if fname == "raise.err":
            raise PermissionError(f"It's not allowed to read {fname}")

        try:
            file = open(fname, "r", encoding='utf-8')
        except FileNotFoundError as e:
            logger.warning(" in inner except, file not found line %s, "
                           "trying adding current filename as prefix.",
                           e.__traceback__.tb_lineno)
            new_fname = __file__[:-2] + fname
            if new_fname == __file__:
                raise UserWarning("Retrying file is the same as myself, "
                                  "skiping") from e
            else:
                file = open(new_fname, "r", encoding='utf-8')
        except Exception as e:
            logger.warning("opening file run into unknown exception %r", e)
            e.add_note(f"ADDED NOTE: Unexpected like opening a dir.")
            raise
    except FileNotFoundError as e:
        logger.error(" in exept block, the file %s was not found, line %s",
                     basename(fname), e.__traceback__.tb_lineno)
    except Exception as e:
        tb_list = []
        current_exception = e
        while current_exception and current_exception.__traceback__:
            tb_info = traceback.extract_tb(current_exception.__traceback__)
            tb_list.extend([f"{current_exception!r} in {funcn}() @{fn}:{ln}"
                            for fn, ln, funcn, _ in tb_info])
            current_exception = current_exception.__cause__ or \
                current_exception.__context__
        tb_list[0:0] = [] if tb_list else [f"{e!r}"]
        stack_count = len(tb_list)
        logger.error("unexpected error %s: %s" + (" <= %s" * (stack_count - 1)),
                     e.__notes__ if hasattr(e, "__notes__") else '', *tb_list)
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
            logger.error("Unexpected error %r, line %s",
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
    print(f"# normal read:{safe_read_file("txt", 16)=}")
    print(f"# Raise warning duplicate with myself:{safe_read_file("py", 16)}")
    print(f"# Raise error read a dir:{safe_read_file("m6_3_package", 16)}")
    print(f"# Raise arbitary Error:{safe_read_file("raise.err", 16)}")


if __name__ == "__main__":
    with log_to(__name__, stream='DEBUG') as logger:
        with open(__file__[:-3] + ".txt", "w", newline='', encoding='utf-8'
                  ) as file_obj:
            print("First Sixteen Characters of a text file.", file=file_obj)
        main(__file__)


#    DEBUG - m8_3_1.py:27 __main__.safe_read_file() - trying to work with file ...txt
#  WARNING - m8_3_1.py:35 __main__.safe_read_file() -  in inner except, file not found line 33, trying adding current filename as prefix.
#    DEBUG - m8_3_1.py:65 __main__.safe_read_file() -  in else block opened file successfully.
#     INFO - m8_3_1.py:80 __main__.safe_read_file() - successfully read 16 chars from txt
#    DEBUG - m8_3_1.py:87 __main__.safe_read_file() -  in finally block: File closed.
# normal read:safe_read_file("txt", 16)='First Sixteen Ch'
#    DEBUG - m8_3_1.py:27 __main__.safe_read_file() - trying to work with file ...py
#  WARNING - m8_3_1.py:35 __main__.safe_read_file() -  in inner except, file not found line 33, trying adding current filename as prefix.
#    ERROR - m8_3_1.py:62 __main__.safe_read_file() - unexpected error : UserWarning('Retrying file is the same as myself, skiping') in safe_read_file() @/m8_3_1.py:40 <= FileNotFoundError(2, 'No such file or directory') in safe_read_file() @/m8_3_1.py:33
#  WARNING - m8_3_1.py:89 __main__.safe_read_file() -  closing py run into exception: UnboundLocalError("cannot access local variable 'file' where it is not associated with a value"), maybe it was never opened?
# Raise warning duplicate with myself:None
#    DEBUG - m8_3_1.py:27 __main__.safe_read_file() - trying to work with file ...m6_3_package
#  WARNING - m8_3_1.py:45 __main__.safe_read_file() - opening file run into unknown exception IsADirectoryError(21, 'Is a directory')
#    ERROR - m8_3_1.py:62 __main__.safe_read_file() - unexpected error ['ADDED NOTE: Unexpected like opening a dir.']: IsADirectoryError(21, 'Is a directory') in safe_read_file() @/m8_3_1.py:33
#  WARNING - m8_3_1.py:89 __main__.safe_read_file() -  closing m6_3_package run into exception: UnboundLocalError("cannot access local variable 'file' where it is not associated with a value"), maybe it was never opened?
# Raise error read a dir:None
#    DEBUG - m8_3_1.py:27 __main__.safe_read_file() - trying to work with file ...raise.err
#    ERROR - m8_3_1.py:62 __main__.safe_read_file() - unexpected error : PermissionError("It's not allowed to read raise.err") in safe_read_file() @/m8_3_1.py:30
#  WARNING - m8_3_1.py:89 __main__.safe_read_file() -  closing raise.err run into exception: UnboundLocalError("cannot access local variable 'file' where it is not associated with a value"), maybe it was never opened?
# Raise arbitary Error:None
#     INFO - m8_2_2.py:66 __main__.logging_context() - shutting down the logging facility...
