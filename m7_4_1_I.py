"""Demo manually process CSV file contents.

Will write then read back a list of list (can be tuple of tuple as well.)
Uses repr to realize quote only strings. 
While reading, cell with quotationmarks will be convert to str, cells without 
quotation marks will be treated as bool or number.

Usage:
    python -m m7_4_1_I

Note:
    This module cannot handle nested quotation marks, escape characters,
    and ill formed float number (i.e. unquoted 1.1.1 will cause an error).
"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)
from os.path import basename

SAMPLE_DATA = [
    ['ID', 'Name', 'Age', 'Grade', 'Pass/Fail'],
    [1, 'Zhang, Alice', 18, 80.5, True],
    [2, 'Yusuf, Bob', 19, 70, True],
    [3, 'Xanders, Carole', 17, 55, False],
    [4, 'West, David', 18, 85.5, True]
]
QUOTE = "'"
DELIMINATOR = ','
NEWLINE = '\n'


def convert_to_csv(obj: any = None) -> str:
    """convert a 2-d iterable object to string of csv.

    This function uses repr() to represent each object within obj. 
    So strings will be quoted using single quotation marks (unless 
    the string contains quotation marks), numbers, bools and None 
    are not quoted.

    Args: 
        obj: a 2-d iterable, of which outer iterable is used as row
            while inner iterable is interpreted as cell.

    Returns:
        a string representation of obj in which newline is the seperation of rows
        and DELIMATOR is used as seperator of cells.
    """
    logger.debug("convert_to_csv() is called with: %80s...", repr(obj)[:80])
    csv_list = []
    for row in obj:
        csv_list.append(DELIMINATOR.join(map(repr, row)))

    return NEWLINE.join(csv_list) + NEWLINE


def convert_from_csv(csv: str) -> list[list]:
    """convert a string representing csv to list of lists.

    This function parse string csv, split by \n to rows and then split by , to 
    cells, it will respect quotation marks QUOTE do not use \n and , within QUOTE 
    to split. It does not handle quotation marks within quotation marks though, it
    does not handle escape sequence either. 

    Args:
        csv: string representing the content of a csv file.

    Returns:
        a list of lists, outer list represent rows, inner list represent cells.
    """
    logger.debug("convert_from_csv() called with: %80s...", repr(csv))

    def str_to_obj(element: str) -> any:
        match element:
            case 'True' | 'False':
                return element == 'True'
            case n if n.isdigit():
                return int(n)
            case s if s.startswith(QUOTE):
                return element.strip(QUOTE)
            case f if f[0].isdigit() or f[0] in '+-':
                return float(f)

    not_in_quote = True
    list_of_list = []
    inner_list = []
    current_element = ''
    for char in csv:
        match char:
            case qt if qt == QUOTE:
                not_in_quote = not not_in_quote
                current_element += qt
            case dl if dl == DELIMINATOR and not_in_quote:
                inner_list.append(str_to_obj(current_element))
                current_element = ''
            case nl if nl == NEWLINE and not_in_quote:
                inner_list.append(str_to_obj(current_element))
                current_element = ''
                list_of_list.append(inner_list)
                inner_list = []
            case _ as c:
                current_element += c

    return list_of_list


def main(file_name: str) -> None:
    """main func demo write/read csv file manually. 

    Args:
        file_name: name of the file to use as csv file.

    """
    csv_file_obj = open(file_name, "w", newline='', encoding='utf-8')
    chars_written = csv_file_obj.write(convert_to_csv(SAMPLE_DATA))
    logger.debug("%s chars (%s)written to %s",
                 chars_written, csv_file_obj.mode, basename(file_name))
    csv_file_obj.close()

    csv_file_obj = open(file_name, "r", newline='', encoding='utf-8')
    file_content = csv_file_obj.read()
    logger.debug("%s chars (%s)read from %s",
                 chars_written, csv_file_obj.mode, basename(file_name))
    csv_file_obj.close()
    csv_content = convert_from_csv(file_content)
    for row in csv_content:
        print("#", row)


if __name__ == '__main__':
    namebase = __file__[:-3]
    filename = namebase + ".data.csv"
    main(filename)

#DEBUG - __main__(m7_4_1_I.py:50) - convert_to_csv() is called with: [['ID', 'Name', 'Age', 'Grade', 'Pass/Fail'], [1, 'Zhang, Alice', 18, 80.5, True...
#DEBUG - __main__(m7_4_1_I.py:117) - 155 chars (w)written to m7_4_1_I.data.csv
#DEBUG - __main__(m7_4_1_I.py:123) - 155 chars (r)read from m7_4_1_I.data.csv
#DEBUG - __main__(m7_4_1_I.py:72) - convert_from_csv() called with: "'ID','Name','Age','Grade','Pass/Fail'\n1,'Zhang, Alice',18,80.5,True\n2,'Yusuf, Bob',19,70,True\n3,'Xanders, Carole',17,55,False\n4,'West, David',18,85.5,True\n"...
# ['ID', 'Name', 'Age', 'Grade', 'Pass/Fail']
# [1, 'Zhang, Alice', 18, 80.5, True]
# [2, 'Yusuf, Bob', 19, 70, True]
# [3, 'Xanders, Carole', 17, 55, False]
# [4, 'West, David', 18, 85.5, True]
