import csv
import json

def main(file_name: str) -> None:
    json_file_obj = open(file_name, "w", newline='', encoding='utf-8')
    student_record_table = [('ID', 'Name', 'Age', 'Grade', 'Pass/Fail'),
                    (1, 'Alice', 18.0, 80.5, True),
                    (2, 'Bob', 19.0, 70.0, True),
                    (3, 'Carole', 17.0, 75.0, True),
                    (4, 'David', 18.0, 85.5, True)]
    student_record_dict = [{'ID': 1, 'Name': 'Alice', 'Age': 18.0, 
                            'Grade': 80.5, 'Pass/Fail': True},
                    {'ID': 2, 'Name': 'Bob', 'Age': 19.0, 
                     'Grade': 70.0, 'Pass/Fail': True},
                    {'ID': 3, 'Name': 'Carole', 'Age': 17.0, 
                     'Grade': 75.0, 'Pass/Fail': True},
                    {'ID': 4, 'Name': 'David', 'Age': 18.0, 
                     'Grade': 85.5, 'Pass/Fail': True}]
    json.dump((student_record_table, student_record_dict), json_file_obj)
    
    json_file_obj.close()

    json_file_obj = open(file_name, "r", newline='', encoding='utf-8')
    stu_rec_tab, stu_rec_dic = json.load(json_file_obj)
    json_file_obj.close()
    for stu_rec in stu_rec_tab:
        print(f"# {type(stu_rec)=}: {stu_rec}")
    for stu_rec in stu_rec_dic:
        print(f"# {type(stu_rec)=}: {stu_rec}")

if __name__ == '__main__':
    base_name = __file__[:-3]
    file_name = (base_name + ".data.json")
    main(file_name)

# type(stu_rec)=<class 'list'>: ['ID', 'Name', 'Age', 'Grade', 'Pass/Fail']
# type(stu_rec)=<class 'list'>: [1, 'Alice', 18.0, 80.5, True]
# type(stu_rec)=<class 'list'>: [2, 'Bob', 19.0, 70.0, True]
# type(stu_rec)=<class 'list'>: [3, 'Carole', 17.0, 75.0, True]
# type(stu_rec)=<class 'list'>: [4, 'David', 18.0, 85.5, True]
# type(stu_rec)=<class 'dict'>: {'ID': 1, 'Name': 'Alice', 'Age': 18.0, 'Grade': 80.5, 'Pass/Fail': True}
# type(stu_rec)=<class 'dict'>: {'ID': 2, 'Name': 'Bob', 'Age': 19.0, 'Grade': 70.0, 'Pass/Fail': True}
# type(stu_rec)=<class 'dict'>: {'ID': 3, 'Name': 'Carole', 'Age': 17.0, 'Grade': 75.0, 'Pass/Fail': True}
# type(stu_rec)=<class 'dict'>: {'ID': 4, 'Name': 'David', 'Age': 18.0, 'Grade': 85.5, 'Pass/Fail': True}
