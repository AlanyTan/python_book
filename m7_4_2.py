"""Demo json.dump and json.load to write/read from json files

Usage: python -m m7_4_2

Note:
    json does not distinguish tuples .vs. lists, so everything saves
    as lists, and while reading, they are all read as lists.    
"""
import json
from m7_4_1_I import SAMPLE_DATA 

def main(file_name: str) -> None:
    """main func save a data structure as json into a text file.
    
    Args:
        file_name: name of the file to be used as the json file
    """
    json_file_obj = open(file_name, "w", encoding='utf-8')
    json.dump(SAMPLE_DATA, json_file_obj)
    json_file_obj.close()

    json_file_obj = open(file_name, "r", encoding='utf-8')
    stu_rec_list = json.load(json_file_obj)
    json_file_obj.close()
    for stu_rec in stu_rec_list:
        print(f"# {type(stu_rec)=}: {stu_rec}")

if __name__ == '__main__':
    base_name = __file__[:-3]
    file_name = (base_name + ".data.json")
    main(file_name)

# type(stu_rec)=<class 'list'>: ['ID', 'Name', 'Age', 'Grade', 'Pass/Fail']
# type(stu_rec)=<class 'list'>: [1, 'Zhang, Alice', 18, 80.5, True]
# type(stu_rec)=<class 'list'>: [2, 'Yusuf, Bob', 19, 70, True]
# type(stu_rec)=<class 'list'>: [3, 'Xanders, Carole', 17, 55, False]
# type(stu_rec)=<class 'list'>: [4, 'West, David', 18, 85.5, True]
