"""Demo csv.DictWriter & csv.DictReader to write/read csv files.

Will call csv.DictWriter to write csv, need to convert bool to str. 
Then call csv.DictReader to read from csv file.

Usage:
    python -m m7_4_1_III

Note:
    bool value need to be converted to str during write, and upon
    read, all numbers are converted to float
"""

import csv
from typing import TextIO
from os.path import basename
import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

from m7_4_1_I import SAMPLE_DATA


def dict_write_csv(file_obj: TextIO,
                   content_dicts: list[dict]) -> None:
    """create csv.DictWriter using the given file_obj, then write
    content_obj as dict to it.

    Args:
        file_obj: a text file opened with newline='',
                    this is where the csv will write into
        header: a list of str representing the column names
        content_dicts: a list of dict each dict represent one row of data

    Returns:
        None.    
    """
    header = {i: None for d in content_dicts for i in d.keys()}.keys()
    csv_writer = csv.DictWriter(file_obj, header, dialect='excel',
                                quoting=csv.QUOTE_NONNUMERIC)
    logger.debug("dict_write_csv(): write(%s) to %s using %s",
                 file_obj.mode, basename(file_obj.name), type(csv_writer))
    csv_writer.writeheader()
    for row in content_dicts:
        csv_writer.writerow(row)


def dict_read_csv(file_obj: TextIO) -> list[dict]:
    """create csv.DictReader using the given file_obj, then read its content.

    Args:
        file_obj: a text file opened with newline='' for read.

    Returns:
        a list of dict contain the csv file content.
    """
    list_of_dict = []
    csv_reader = csv.DictReader(file_obj, dialect='excel',
                                quoting=csv.QUOTE_NONNUMERIC)
    logger.debug("dict_read_csv(): reading(%s) from %s using %s",
                 file_obj.mode, basename(file_obj.name), type(csv_reader))
    for row in csv_reader:
        list_of_dict.append(row)
    return list_of_dict


def main(file_name: str) -> None:
    """main func demo write/read csv using csv.DictWriter & csv.DictReader

    This will get a list_of_dict from dict_read_csv(), this allows us to 
    use row number and column name to retrieve a value like:
    data_table[2]['Grade']

    Args:
        file_name: name of the file to use as csv file

    """
    csv_file_obj = open(file_name, "w", newline='', encoding='utf-8')
    SAMPLE_DATA_LIST_OF_DICT = [dict(zip(SAMPLE_DATA[0],
                                         [str(item) if isinstance(item, bool)
                                          else item for item in row]))
                                for row in SAMPLE_DATA[1:]]
    dict_write_csv(csv_file_obj, SAMPLE_DATA_LIST_OF_DICT)
    csv_file_obj.close()

    csv_file_obj = open(file_name, "r", newline='', encoding='utf-8')
    data_table = dict_read_csv(csv_file_obj)
    csv_file_obj.close()
    for row in data_table:
        print("#", row)

    print(f"# Retrieve Grade of #3 student: {data_table[2]['Grade']}")


if __name__ == '__main__':
    namebase = __file__[:-3]
    filename = (namebase + ".data.csv")
    main(filename)

#DEBUG - __main__(m7_4_1_III.py:41) - dict_write_csv(): write(w) to m7_4_1_III.data.csv using <class 'csv.DictWriter'>
#DEBUG - __main__(m7_4_1_III.py:60) - dict_read_csv(): reading(r) from m7_4_1_III.data.csv using <class 'csv.DictReader'>
# {'ID': 1.0, 'Name': 'Zhang, Alice', 'Age': 18.0, 'Grade': 80.5, 'Pass/Fail': 'True'}
# {'ID': 2.0, 'Name': 'Yusuf, Bob', 'Age': 19.0, 'Grade': 70.0, 'Pass/Fail': 'True'}
# {'ID': 3.0, 'Name': 'Xanders, Carole', 'Age': 17.0, 'Grade': 55.0, 'Pass/Fail': 'False'}
# {'ID': 4.0, 'Name': 'West, David', 'Age': 18.0, 'Grade': 85.5, 'Pass/Fail': 'True'}
# Retrieve Grade of #3 student: 55.0
