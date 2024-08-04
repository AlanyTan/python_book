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
import io
import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

from m7_4_1_I import SAMPLE_DATA

def dict_write_csv(file_obj: io.BufferedReader, header: list[str],
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
    csv_writer = csv.DictWriter(file_obj, header, dialect='excel', 
                                quoting=csv.QUOTE_NONNUMERIC)
    logger.debug(f"dict_write_csv() called:{file_obj.name.split('\\')[-1]}, "
                 f"{str(header):.80s}, {len(content_dicts)} rows to be written"
                 f"({file_obj.mode}) using {type(csv_writer)}.")
    csv_writer.writeheader()
    for row in content_dicts:
        csv_writer.writerow(row)

def dict_read_csv(file_obj: io.BufferedReader) -> dict:
    """create csv.DictReader using the given file_obj, then read its content.
    
    Args:
        file_obj: a text file opened with newline='' for read.
        
    Returns:
        a list of dict contain the csv file content.
    """
    list_of_dict = []
    csv_reader = csv.DictReader(file_obj, dialect='excel', 
                                quoting=csv.QUOTE_NONNUMERIC)
    logger.debug(f"dict_read_csv() called: {file_obj.name.split('\\')[-1]}, "
                 f"reading({file_obj.mode}) using {type(csv_reader)}.")
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
    dict_write_csv(csv_file_obj, SAMPLE_DATA[0],
                   [dict(zip(SAMPLE_DATA[0],
                             [str(item) if isinstance(item, bool) else item
                              for item in row]))
                    for row in SAMPLE_DATA[1:]])
    csv_file_obj.close()

    csv_file_obj = open(file_name, "r", newline='', encoding='utf-8')
    data_table = dict_read_csv(csv_file_obj)
    csv_file_obj.close()
    for row in data_table:
        print("#", row)
    
    print(f"# Retrieve Grade of #3 student: {data_table[2]['Grade']}")


if __name__ == '__main__':
    base_name = __file__[:-3]
    file_name = (base_name + ".data.csv")
    main(file_name)

#DEBUG - __main__(m7_4_1_III.py:39) - dict_write_csv() called:m7_4_1_III.data.csv, ['ID', 'Name', 'Age', 'Grade', 'Pass/Fail'], 4 rows to be written(w) using <class 'csv.DictWriter'>.
#DEBUG - __main__(m7_4_1_III.py:58) - dict_read_csv() called: m7_4_1_III.data.csv, reading(r) using <class 'csv.DictReader'>.
# {'ID': 1.0, 'Name': 'Zhang, Alice', 'Age': 18.0, 'Grade': 80.5, 'Pass/Fail': 'True'}
# {'ID': 2.0, 'Name': 'Yusuf, Bob', 'Age': 19.0, 'Grade': 70.0, 'Pass/Fail': 'True'}
# {'ID': 3.0, 'Name': 'Xanders, Carole', 'Age': 17.0, 'Grade': 55.0, 'Pass/Fail': 'False'}
# {'ID': 4.0, 'Name': 'West, David', 'Age': 18.0, 'Grade': 85.5, 'Pass/Fail': 'True'}
# Retrieve Grade of #3 student: 55.0
