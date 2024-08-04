"""Demo with structure inside try-except."""
import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

def safe_read_file(fname: str) -> str:
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
        logger.debug(f"trying to work with ...{fname[-16:]}")
        with open(fname, "r") as file:
            logger.debug(f" file opened as {type(file)}")
            data = file.readline()
            texts = data.strip()
        logger.debug(f" finished file reading with. {file.closed=}")
        return texts
    except FileNotFoundError as e:
        logger.error(f"The file {fname} was not found {'file' in dir()=}"
                     f", line {e.__traceback__.tb_lineno}, ")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}"
                     f", line {e.__traceback__.tb_lineno}, ")

def main(fnames: list[str]) -> None:
    """main func demo sending different denominators to save_divide.
    
    Args:
        list_of_numbers_to_try: a list containing numbers to be used
        as denominator when trying to call save_divide.
    """
    for fname in fnames:
        print(f"#1st line of text in file:{safe_read_file(fname)}")

if __name__ == "__main__":
    file_names = [__file__, "example.txt"]
    main(file_names)
    
#DEBUG - __main__(m8_2_1.py:23) - trying to work with ...n_book\m8_2_1.py
#DEBUG - __main__(m8_2_1.py:25) -  file opened as <class '_io.TextIOWrapper'>
#DEBUG - __main__(m8_2_1.py:28) -  finished file reading with. file.closed=True
#1st line of text in file:"""Demo with structure inside try-except."""
#DEBUG - __main__(m8_2_1.py:23) - trying to work with ...example.txt
#ERROR - __main__(m8_2_1.py:31) - The file example.txt was not found 'file' in dir()=False, line 24, 
#1st line of text in file:None
