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
from m7_4_1_I import SAMPLE_DATA

def write_csv(file_obj: io.BufferedReader, content_obj: any = None) -> None:
    """create csv.writer using the given file_obj, then write content_obj to it.
    
    Args:
        file_obj: a text file opened with newline='', this is where the csv will write into
        content_obj: a 2d iterable contain data to be saved into csv.

    Returns:
        None.    
    """
    csv_writer = csv.writer(file_obj, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
    print(f"# open csv for {file_obj.mode}, use {type(csv_writer)=} to write into it.")
    for row in content_obj if content_obj else SAMPLE_DATA:
        csv_writer.writerow([str(item) if isinstance(item, bool) else item for item in row])

def read_csv(file_obj: io.BufferedReader) -> list[list]:
    """create csv.reader using the given file_obj, then read its content.
    
    Args:
        file_obj: a text file opened with newline='' for read.
        
    Returns:
        a list of lists contain the csv file content.
    """
    list_of_list = []
    csv_reader = csv.reader(file_obj, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
    print(f"# open csv for {file_obj.mode}, use {type(csv_reader)=} to read from it.")
    for row in csv_reader:
        list_of_list.append(row)
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
    base_name = __file__[:-3]
    file_name = (base_name + ".data.csv")
    main(file_name)

# open csv for w, use type(csv_writer)=<class '_csv.writer'> to write into it.
# open csv for r, use type(csv_reader)=<class '_csv.reader'> to read from it.
# ['ID', 'Name', 'Age', 'Grade', 'Pass/Fail']
# [1.0, 'Zhang, Alice', 18.0, 80.5, 'True']
# [2.0, 'Yusuf, Bob', 19.0, 70.0, 'True']
# [3.0, 'Xanders, Carole', 17.0, 55.0, 'False']
# [4.0, 'West, David', 18.0, 85.5, 'True']
    