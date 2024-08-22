"""Demo csv.writer & csv.reader to write/read csv files.

Will call csv.writer to write csv, need to convert bool to str. 
Then call csv.reader to read from csv file.

Usage:
    python -m m7_4_1_II

Note:
    bool value need to be converted to str during write, and upon
    read, all numbers are converted to float
"""
import csv
import io
from os.path import basename
import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

from m7_4_1_I import SAMPLE_DATA


def write_csv(file_obj: io.BufferedReader, content_obj: any = None) -> None:
    """create csv.writer using the given file_obj, then write content_obj to it.

    Args:
        file_obj: a text file opened with newline='', this is where the csv will write into
        content_obj: a 2d iterable contain data to be saved into csv.

    Returns:
        None.    
    """
    logger.debug("write_csv() called with: %s(%s), %80r",
                 basename(file_obj.name), file_obj.mode, content_obj)
    csv_writer = csv.writer(file_obj, dialect='excel',
                            quoting=csv.QUOTE_NONNUMERIC)
    csv_writer.writerows([[str(item) if isinstance(item, bool) else item
                           for item in row] for row in content_obj])
    # ***Or replace the previous statement with the following for loop***
    #for row in content_obj:
    #    csv_writer.writerow([str(item) if isinstance(
    #        item, bool) else item for item in row])


def read_csv(file_obj: io.BufferedReader) -> list[list]:
    """create csv.reader using the given file_obj, then read its content.

    Args:
        file_obj: a text file opened with newline='' for read.

    Returns:
        a list of lists contain the csv file content.
    """
    logger.debug("read_csv() called with: %s(%s)",
                 basename(file_obj.name), file_obj.mode)
    list_of_list = []
    csv_reader = csv.reader(file_obj, dialect='excel',
                            quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        list_of_list.append(row)
    logger.debug("read_csv will return: %80r", list_of_list)
    return list_of_list


def main(file_name: str) -> None:
    """main func demo write/read csv using csv.writer & csv.reader.

    Args:
        file_name: name of the file to use as csv file

    """
    csv_file_obj = open(file_name, "w", newline='', encoding='utf-8')
    write_csv(csv_file_obj, SAMPLE_DATA)
    csv_file_obj.close()

    csv_file_obj = open(file_name, "r", newline='', encoding='utf-8')
    for row in read_csv(csv_file_obj):
        print(f"# {row}")

    csv_file_obj.close()


if __name__ == '__main__':
    namebase = __file__[:-3]
    filename = namebase + ".data.csv"
    main(filename)

#DEBUG - __main__(m7_4_1_II.py:32) - write_csv() called with: m7_4_1_II.data.csv(w), [['ID', 'Name', 'Age', 'Grade', 'Pass/Fail'], [1, 'Zhang, Alice', 18, 80.5, True...
#DEBUG - __main__(m7_4_1_II.py:47) - read_csv() called with: m7_4_1_II.data.csv(r)
#DEBUG - __main__(m7_4_1_II.py:53) - read_csv will return [['ID', 'Name', 'Age', 'Grade', 'Pass/Fail'], [1.0, 'Zhang, Alice', 18.0, 80.5, ...
# ['ID', 'Name', 'Age', 'Grade', 'Pass/Fail']
# [1.0, 'Zhang, Alice', 18.0, 80.5, 'True']
# [2.0, 'Yusuf, Bob', 19.0, 70.0, 'True']
# [3.0, 'Xanders, Carole', 17.0, 55.0, 'False']
# [4.0, 'West, David', 18.0, 85.5, 'True']
