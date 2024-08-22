"""Module demonstrate read text file line by line with for loop.
When run as main, this module first call the m7_3_3.write_to_file()
to create a text file, then read every line of it using for loop.

Usage: 
    python -m m7_3_1

"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

from m7_2_3 import write_to_file


def main(file_name: str) -> None:
    """Demo using for loop to read every line of a text file

    Args:
        file_name: the name of the text file to read.

    Returns:
        None
    """
    file_r = open(file_name, 'r', encoding='utf-8')
    logger.debug("opened file: %s", file_r)
    for line in file_r:
        print(f"# {line=}")

    file_r.close()


if __name__ == "__main__":
    namebase = __file__[:-3]
    filename = namebase + ".data.txt"
    logger.debug("calling write_to_file to prepare for file to read")
    write_to_file(filename, 't', 'utf-8')
    main(filename)

#DEBUG - __main__(m7_3_1.py:38) - calling write_to_file to prepare for file to read
#DEBUG - m7_2_3(m7_2_3.py:33) - entering write_to_file(...m7_3_1.data.txt, t, utf-8)...
#DEBUG - m7_2_3(m7_2_3.py:47) - processing data as text.
#DEBUG - m7_2_3(m7_2_3.py:54) - writelines() to text file: ['Python程序设计', 2, False, 'A string literal.']
#DEBUG - m7_2_3(m7_2_3.py:57) - file {'...m7_3_1.data.txt'} closed.
#DEBUG - __main__(m7_3_1.py:28) - opened file:<_io.TextIOWrapper name='C:\\Users\\user\\Documents\\python_book\\m7_3_1.data.txt' mode='r' encoding='utf-8'>
# line='Python程序设计\n'
# line='2\n'
# line='False\n'
# line='A string literal.\n'
