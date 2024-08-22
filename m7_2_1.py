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
    logger.debug("file %s opened for write...", file_name)
    print("Saving text:", text_info, file=file_obj)
    print("Saving number:", int_info, file=file_obj)
    print("Saving boolean:", bool_info, file=file_obj)
    print(f"into file {file_name}", file=file_obj)
    logger.debug("data have been written into file %s.", file_name)
    file_obj.close()
    logger.debug("file %s closed.", file_name)


if __name__ == "__main__":
    namebase = __file__[:-3]
    filename = namebase + ".data.txt"
    main(filename)

#DEBUG - __main__(m7_2_1.py:25) - file /workspaces/python-book/m7_2_1.data.txt opened for write...
#DEBUG - __main__(m7_2_1.py:30) - data have been written into file /workspaces/python-book/m7_2_1.data.txt.
#DEBUG - __main__(m7_2_1.py:32) - file /workspaces/python-book/m7_2_1.data.txt closed.
