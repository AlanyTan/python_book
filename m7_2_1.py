"""print() info into textfile"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

def main(file_name: str) -> None:
    """Main func demo print() into text file.

    Will print an int, a bool, a str variable and a str literal to
    a text file opened using file_name given.
    
    Args:
        file_name: string representing file name to create and open.

    Returns: 
        None
    """
    int_info = 2
    bool_info = True
    text_info = "text content containing 2 & True"
    file_obj = open(file_name, 'w+', encoding='utf-8')
    logger.debug(f"file {file_name} opened for write...")
    print("Saving text:", text_info, file=file_obj)
    print("Saving number:", int_info, file=file_obj)
    print("Saving boolean:", bool_info, file=file_obj)
    print(f"into file {file_name}", file=file_obj)
    logger.debug(f"data have been written into file {file_name}.")
    file_obj.close()
    logger.debug(f"file {file_name} closed.")


if __name__ == "__main__":
    base_name = __file__[:-3]
    file_name = base_name + ".data.txt"
    main(file_name)
    
#DEBUG - __main__(m7_2_1.py:24) - file C:\Users\user\Documents\python_book\m7_2_1.data.txt opened for write...
#DEBUG - __main__(m7_2_1.py:29) - data have been written into file C:\Users\user\Documents\python_book\m7_2_1.data.txt.
#DEBUG - __main__(m7_2_1.py:31) - file C:\Users\user\Documents\python_book\m7_2_1.data.txt closed.
