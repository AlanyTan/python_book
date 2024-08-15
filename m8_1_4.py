"""Demo try-except-else-finally structure"""
import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

def safe_read_file(fname: str) -> str:
    """open the given filename, read it's first line, and return it. 
    
    It tries to open the given filename, and read the first line, 
    if run into exception, will report the error, otherwise, report
    the read is finished properly.
    
    Args:
        fname: string representing the file name to open.
    
    Returns:
        the first line of the file as a stirng.
    """
    try:
        logger.debug(f"trying to work with file ...{fname[-16:]}")
        file = None
        file = open(fname, "r")
        data = file.readline()
    except FileNotFoundError as e:
        logger.error(f" file {fname} was not found"
                     f", line {e.__traceback__.tb_lineno}")
    except Exception as e:
        logger.error(f" An unexpected error occurred: {repr(e)}"
                     f", line {e.__traceback__.tb_lineno}")
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
    
#DEBUG - __main__(m8_1_4.py:21) - trying to work with file ...n_book\m8_1_4.py
#INFO - __main__(m8_1_4.py:32) -  in the else block (finished reading file properly)
#INFO - __main__(m8_1_4.py:37) -  in the finally block: File closed.
# 1st line of text in file:"""Demo try-except-else-finally structure"""
#DEBUG - __main__(m8_1_4.py:21) - trying to work with file ...donot.exist
#ERROR - __main__(m8_1_4.py:26) -  file donot.exist was not found, line 23
#INFO - __main__(m8_1_4.py:39) -  in the finally block, File was never opened.
#ERROR - __main__(m8_1_4.py:41) -   !func safe_read_file ended with errors.
# 1st line of text in file:None
#INFO - __main__(m8_1_4.py:57) - shutting down logging.
