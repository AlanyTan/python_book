"""Demonstrate using .readlines() and list operations to process file content.

This module realize the same functionality as m7_3_1_I, but replace sequential 
line processing with .readlines() and list, and generators.

Usage: 
    python -m m7_3_3

Note:
    This module will create a test file under the current directory, 
    so please make sure you have write permission in the current dir.
"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

from m7_3_2 import creat_input_file, EXAMPLE_CONTENT

SKIP_WORDS = ['skip']


def parse_line(line: str) -> list:
    """Parse a line based on logic in section 3.4

    For each char in the given line, add its ASCII code to return list.
    Unless it's a '.' or '!' which will abort and ignore everything after it.
    If the line is '\n' or only contain words in the SKIP_WORD list, then 
    the result list will be empty.

    Args:
        line: the str that contains characters to be processed.

    Returns:
        A list of str, each shows the char and its ASCII code.
    """
    logger.debug("parsing line %r", line)
    result = []
    line = line.strip('\n')
    if line := '' if line in SKIP_WORDS else line:
        result.append(f" Read: {line}")

    for letter in line:
        match letter:
            case '.':
                result.append("..Reached period, ignore the rest.")
                break
            case '!':
                result.append(
                    "!!Reached exclaimation mark, abort processing!")
                break
            case _:
                result.append(f"   {letter}'s ASCII code is {ord(letter)}")
    return result


def main(file_name: str) -> None:
    """Demo using .readlines() read full content from file and batch process.

    This function demonstrate using .readlines() to read file lines into
    a list, and use list, map, generator to process the content, but 
    realize the program behavior.

    Args:
        file_name: the name of the text file to use.

    Returns:
        None
    """
    file_r = open(file_name, 'r', encoding='utf-8')
    logger.debug("input file %s opened for reading", file_name[-15:])
    count = 0
    for result in map(parse_line, file_r.readlines(1048576)):
        if result:
            print(*result, sep='\n#')
            count += 1
        if "!!Reached exclaimation mark, abort processing!" in result:
            break

    print(f"## Processed {count} strings in total")
    file_r.close()


if __name__ == "__main__":
    namebase = __file__[:-3]
    filename = namebase + ".data.txt"
    if creat_input_file(filename, EXAMPLE_CONTENT):
        logger.debug("input file %s created", filename[-15:])
        main(filename)

#DEBUG - __main__(m7_3_3.py:89) - input file m7_3_3.data.txt created
#DEBUG - __main__(m7_3_3.py:72) - input file m7_3_3.data.txt opened for reading
#DEBUG - __main__(m7_3_3.py:38) - parsing line 'abc.def\n'
# Read: abc.def
#   a's ASCII code is 97
#   b's ASCII code is 98
#   c's ASCII code is 99
#..Reached period, ignore the rest.
#DEBUG - __main__(m7_3_3.py:38) - parsing line '\n'
#DEBUG - __main__(m7_3_3.py:38) - parsing line 'skip\n'
#DEBUG - __main__(m7_3_3.py:38) - parsing line '123\n'
# Read: 123
#   1's ASCII code is 49
#   2's ASCII code is 50
#   3's ASCII code is 51
# Processed 2 strings in total
