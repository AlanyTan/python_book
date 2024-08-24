"""Demo raise..., raise ... from e, and raise.

Usage:
    python m8_3_1.py
"""

from os.path import basename
import m7_4_1_II
from m8_2_2 import logging_context as log_to
import traceback


def safe_read_file(fname: str, size: int) -> str | None:
    """open the given filename, read it's first line, and return it. 

    It tries to open the given filename, and read the first line, 
    if fname is not found, it tries to treat fname as extention name
    and look for a file with same prefix as current program file. 

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
        tb_info = []
        current_exception = e
        while current_exception and current_exception.__traceback__:
            tb_info.extend(
                traceback.extract_tb(current_exception.__traceback__))
            current_exception = current_exception.__cause__ or \
                current_exception.__context__
        stack_count = len(tb_info)
        logger.error("unexpected error (%s %s)" + (" @ %s" * stack_count),
                     e, e.__notes__ if hasattr(e, "__notes__") else '',
                     *[f"{funcname}() at {filen}:{ln}"
                       for (filen, ln, funcname, _) in tb_info])
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
    print(f"# normal read:{safe_read_file("csv", 16)=}")
    print(f"# Raise warning duplicate with myself:{safe_read_file("py", 16)}")
    print(f"# Raise error read a dir:{safe_read_file("m6_3_package", 16)}")
    print(f"# Raise arbitary Error:{safe_read_file("raise.err", 16)}")


if __name__ == "__main__":
    with open(__file__[:-3] + ".csv", "w", newline='', encoding='utf-8'
              ) as csv_file_obj:
        m7_4_1_II.write_csv(csv_file_obj, m7_4_1_II.SAMPLE_DATA)
    with log_to(__name__, stream='') as logger:
        main(__file__)

#DEBUG - m7_4_1_II(m7_4_1_II.py:34) - write_csv() called with: m8_3_1.csv(w), [['ID', 'Name', 'Age', 'Grade', 'Pass/Fail'], [1, 'Zhang, Alice', 18, 80.5, True], [2, 'Yusuf, Bob', 19, 70, True], [3, 'Xanders, Carole', 17, 55, False], [4, 'West, David', 18, 85.5, True]]
#DEBUG - __main__(m8_3_1.py:27) - trying to work with file ...csv
#WARNING - __main__(m8_3_1.py:35) -  in inner except, file not found line 33, trying adding current filename as prefix.
#DEBUG - __main__(m8_3_1.py:65) -  in else block opened file successfully.
#INFO - __main__(m8_3_1.py:80) - successfully read 16 chars from csv
#DEBUG - __main__(m8_3_1.py:87) -  in finally block: File closed.
# normal read:safe_read_file("csv", 16)='"ID","Name","Age'
#DEBUG - __main__(m8_3_1.py:27) - trying to work with file ...py
#WARNING - __main__(m8_3_1.py:35) -  in inner except, file not found line 33, trying adding current filename as prefix.
#ERROR - __main__(m8_3_1.py:60) - unexpected error (Retrying file is the same as myself, skiping ) @ safe_read_file() at m8_3_1.py:40 @ safe_read_file() at m8_3_1.py:33
#WARNING - __main__(m8_3_1.py:89) -  closing py run into exception: UnboundLocalError("cannot access local variable 'file' where it is not associated with a value"), maybe it was never opened?
# Raise warning duplicate with myself:None
#DEBUG - __main__(m8_3_1.py:27) - trying to work with file ...m6_3_package
#WARNING - __main__(m8_3_1.py:45) - opening file run into unknown exception IsADirectoryError(21, 'Is a directory')
#ERROR - __main__(m8_3_1.py:60) - unexpected error ([Errno 21] Is a directory: 'm6_3_package' ['ADDED NOTE: Unexpected like opening a dir.']) @ safe_read_file() at /workspaces/python-book/m8_3_1.py:33
#WARNING - __main__(m8_3_1.py:89) -  closing m6_3_package run into exception: UnboundLocalError("cannot access local variable 'file' where it is not associated with a value"), maybe it was never opened?
# Raise error read a dir:None
#DEBUG - __main__(m8_3_1.py:27) - trying to work with file ...raise.err
#ERROR - __main__(m8_3_1.py:60) - unexpected error (It's not allowed to read raise.err ) @ safe_read_file() at /workspaces/python-book/m8_3_1.py:30
#WARNING - __main__(m8_3_1.py:89) -  closing raise.err run into exception: UnboundLocalError("cannot access local variable 'file' where it is not associated with a value"), maybe it was never opened?
# Raise arbitary Error:None
