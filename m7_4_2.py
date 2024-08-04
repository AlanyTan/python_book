"""Demo json.dump and json.load to write/read from json files

Usage: python -m m7_4_2

Note:
    json does not distinguish tuples .vs. lists, so everything saves
    as lists, and while reading, they are all read as lists.    
"""
import json
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
    logger.debug(f"data has been dumped to {file_name.split('\\')[-1]}.")
    json_file_obj.close()

    json_file_obj = open(file_name, "r", encoding='utf-8')
    logger.debug(f"{file_name.split('\\')[-1]} opened, will load data...")
    stu_rec_list = json.load(json_file_obj)
    json_file_obj.close()
    logger.debug(f"loaded data is {stu_rec_list=}")
    for stu_rec in stu_rec_list:
        print("# {:2}|{:15}|{:3}|{:5}|{!s:9}|".format(*stu_rec))

if __name__ == '__main__':
    base_name = __file__[:-3]
    file_name = (base_name + ".data.json")
    main(file_name)

#DEBUG - __main__(m7_4_2.py:25) - data has been dumped to m7_4_2.data.json.
#DEBUG - __main__(m7_4_2.py:29) - m7_4_2.data.json opened, will load data...
#DEBUG - __main__(m7_4_2.py:32) - loaded data is stu_rec_list=[['ID', 'Name', 'Age', 'Grade', 'Pass/Fail'], [1, 'Zhang, Alice', 18, 80.5, True], [2, 'Yusuf, Bob', 19, 70, True], [3, 'Xanders, Carole', 17, 55, False], [4, 'West, David', 18, 85.5, True]]
# ID|Name           |Age|Grade|Pass/Fail|
#  1|Zhang, Alice   | 18| 80.5|        1|
#  2|Yusuf, Bob     | 19|   70|        1|
#  3|Xanders, Carole| 17|   55|        0|
#  4|West, David    | 18| 85.5|        1|
