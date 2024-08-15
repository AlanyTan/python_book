"""Demo nested try-except structure"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

def safe_read_file(fname: str, size: int) -> str:
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
    try:
        logger.debug(f"trying to work with file ...{fname[-16:]}")
        file = open(fname, "r")
        try:
            data = file.read(size)
        except TypeError as e:
            logger.warning(f"reading {size} chars from {fname[-16]} failed."
                     f" with {repr(e)}, line {e.__traceback__.tb_lineno}, "
                    "try reading the first line instead.")
            data = file.readline().strip()
        except Exception as e:
            logger.error(f"unexpected error {repr(e)}"
                     f", line {e.__traceback__.tb_lineno}, ")
            data = None
        else:
            logger.info(f"successfully read {size} chars from {fname[-16]}")
            
    except FileNotFoundError as e:
        logger.error(f" in exept block, the file {fname} was not found"
                     f", line {e.__traceback__.tb_lineno}")   
    except Exception as e:
        logger.error(f" An unexpected error occurred: {e}"
                     f", line {e.__traceback__.tb_lineno}")
    else:
        logger.info(" in else block finished reading file properly.")
        return data
    finally:
        try:
            file.close()
            logger.info(" in finally block: File closed.")
        except Exception as e:
            logger.warning(f" closing {fname=} run into exception,{e}, "
                        "maybe it was never opened?")

def main(fname: str) -> None:
    """main func demo sending different denominators to save_divide.
    
    Args:
        list_of_numbers_to_try: a list containing numbers to be used
        as denominator when trying to call save_divide.
    """
    print(f"# first 16 chars of  file:{safe_read_file(fname, 16)}")
    print(f"# wrong type of size in file:{safe_read_file(fname, 'sixteen')}")
    print(f"# non-exist file:{safe_read_file('donot.exist', 0)}")

if __name__ == "__main__":
    try:
        file_name = __file__
        main(file_name)
    finally:
        logger.info("shutting down logging.")
        logging.shutdown()
        
#DEBUG - __main__(m8_1_5.py:24) - trying to work with file ...n_book\m8_1_5.py
#INFO - __main__(m8_1_5.py:38) - successfully read 16 chars from n
#INFO - __main__(m8_1_5.py:47) -  in else block finished reading file properly.
#INFO - __main__(m8_1_5.py:52) -  in finally block: File closed.
# first 16 chars of  file:"""Demo nested t
#DEBUG - __main__(m8_1_5.py:24) - trying to work with file ...n_book\m8_1_5.py
#WARNING - __main__(m8_1_5.py:29) - reading sixteen chars from n failed. with TypeError("argument should be integer or None, not 'str'"), line 27, try reading the first line instead.
#INFO - __main__(m8_1_5.py:47) -  in else block finished reading file properly.
#INFO - __main__(m8_1_5.py:52) -  in finally block: File closed.
# wrong type of size in file:"""Demo nested try-except structure"""
#DEBUG - __main__(m8_1_5.py:24) - trying to work with file ...donot.exist
#ERROR - __main__(m8_1_5.py:41) -  in exept block, the file donot.exist was not found, line 25
#WARNING - __main__(m8_1_5.py:54) -  closing fname='donot.exist' run into exception,cannot access local variable 'file' where it is not associated with a value, maybe it was never opened?
# non-exist file:None
#INFO - __main__(m8_1_5.py:73) - shutting down logging.
