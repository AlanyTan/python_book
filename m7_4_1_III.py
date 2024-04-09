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
from m7_4_1_I import SAMPLE_DATA

def dict_write_csv(file_obj: io.BufferedReader, content_obj: any = None) -> None:
    """create csv.DictWriter using the given file_obj, then write content_obj as dict to it.
    
    Args:
        file_obj: a text file opened with newline='', this is where the csv will write into
        content_obj: a 2d iterable contain data to be saved into csv.

    Returns:
        None.    
    """
    if content_obj is None:
        content_obj = SAMPLE_DATA
    csv_writer = csv.DictWriter(file_obj, content_obj[0], dialect='excel', 
                                quoting=csv.QUOTE_NONNUMERIC)
    print(f"# open csv for {file_obj.mode}, use {type(csv_writer)=} to write into it.")
    csv_writer.writeheader()
    for row in content_obj[1:]:
        row_bool_to_str = [str(item) if isinstance(item, bool) else item for item in row]
        csv_writer.writerow(dict(zip(content_obj[0], row_bool_to_str)))

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
    print(f"# open csv for {file_obj.mode}, use {type(csv_reader)=} to read from it.")
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
    dict_write_csv(csv_file_obj, SAMPLE_DATA)
    csv_file_obj.close()

    csv_file_obj = open(file_name, "r", newline='', encoding='utf-8')
    csv_reader = csv.DictReader(csv_file_obj, dialect='excel', 
                                quoting=csv.QUOTE_NONNUMERIC)
    data_table = dict_read_csv(csv_file_obj)
    for row in data_table:
        print("#", row)
    
    print(f"# Locate Grade of #3 student: {data_table[2]['Grade']}")
        
    csv_file_obj.close()

if __name__ == '__main__':
    base_name = __file__[:-3]
    file_name = (base_name + ".data.csv")
    main(file_name)

# open csv for w, use type(csv_writer)=<class 'csv.DictWriter'> to write into it.
# open csv for r, use type(csv_reader)=<class 'csv.DictReader'> to read from it.
# {'ID': 1.0, 'Name': 'Zhang, Alice', 'Age': 18.0, 'Grade': 80.5, 'Pass/Fail': 'True'}
# {'ID': 2.0, 'Name': 'Yusuf, Bob', 'Age': 19.0, 'Grade': 70.0, 'Pass/Fail': 'True'}
# {'ID': 3.0, 'Name': 'Xanders, Carole', 'Age': 17.0, 'Grade': 55.0, 'Pass/Fail': 'False'}
# {'ID': 4.0, 'Name': 'West, David', 'Age': 18.0, 'Grade': 85.5, 'Pass/Fail': 'True'}
# Locate Grade of #3 student: 55.0
