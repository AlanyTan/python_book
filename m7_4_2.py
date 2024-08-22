"""Demo json.dump and json.load to write/read from json files

Usage: python -m m7_4_2

Note:
    json does not distinguish tuples .vs. lists, so everything saves
    as lists, and while reading, they are all read as lists.    
"""
import json
from os.path import basename
import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

from m7_4_1_I import SAMPLE_DATA


def main(file_name: str) -> None:
    """main func save a data structure as json into a text file.

    Args:
        file_name: name of the file to be used as the json file
    """
    json_file_obj = open(file_name, "w", encoding='utf-8')
    json.dump(SAMPLE_DATA, json_file_obj)
    logger.debug("data has been dumped into %s", basename(file_name))
    json_file_obj.close()

    json_file_obj = open(file_name, "r", encoding='utf-8')
    logger.debug("opened %s for read, will load data...", basename(file_name))
    stu_rec_list = json.load(json_file_obj)
    json_file_obj.close()
    logger.debug("loaded data is %r", stu_rec_list)
    for stu_rec in stu_rec_list:
        print("# {:2}|{:15}|{:3}|{:5}|{!s:9}|".format(*stu_rec))


if __name__ == '__main__':
    namebase = __file__[:-3]
    filename = (namebase + ".data.json")
    main(filename)

#DEBUG - __main__(m7_4_2.py:27) - data has been dumped into m7_4_2.data.json
#DEBUG - __main__(m7_4_2.py:31) - opened m7_4_2.data.json for read, will load data...
#DEBUG - __main__(m7_4_2.py:34) - loaded data is [['ID', 'Name', 'Age', 'Grade', 'Pass/Fail'], [1, 'Zhang, Alice', 18, 80.5, True], [2, 'Yusuf, Bob', 19, 70, True], [3, 'Xanders, Carole', 17, 55, False], [4, 'West, David', 18, 85.5, True]]
# ID|Name           |Age|Grade|Pass/Fail|
#  1|Zhang, Alice   | 18| 80.5|True     |
#  2|Yusuf, Bob     | 19|   70|True     |
#  3|Xanders, Carole| 17|   55|False    |
#  4|West, David    | 18| 85.5|True     |
