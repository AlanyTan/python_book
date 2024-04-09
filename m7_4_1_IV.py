"""Demo csv.Sniffer() ability to guess csv dialect.

Usage:
    python -m m7_4_1_IV

Note:
    depends on m7_4_1_II, which in turn depends on m7_4_1_I.
"""
import csv
import m7_4_1_II

def main(file_name: str) -> None:
    """main func showing csv.Sniffer() guess header and dialect.
    
    Args:
        file_name: string representing filename to use.
    """
    csv_file_obj = open(file_name, "w", newline='', encoding='utf-8')
    m7_4_1_II.write_csv(csv_file_obj)
    csv_file_obj.close()

    csv_file_obj = open(file_name, "r", newline='', encoding='utf-8')
    csv_beginning = csv_file_obj.read(1024)
    csv_file_obj.seek(0)
    csv_has_header = csv.Sniffer().has_header(csv_beginning)
    csv_dialect = csv.Sniffer().sniff(csv_beginning)
    print(f"# csv has header: {csv_has_header}, csv dialect: {csv_dialect}")
    csv_reader = csv.reader(csv_file_obj, dialect=csv_dialect,
                            quoting=csv.QUOTE_NONNUMERIC)
    print(f"# open csv for {csv_file_obj.mode}, use {type(csv_reader)=}")
    data_table = []
    for row in csv_reader:
        print("#", row)
        data_table.append(row)
    
    print(f"# Locate Grade of #3 student: {data_table[2+csv_has_header][3]}")
        
    csv_file_obj.close()

if __name__ == '__main__':
    base_name = __file__[:-3]
    file_name = (base_name + ".data.csv")
    main(file_name)

# open csv for w, use type(csv_writer)=<class 'csv.DictWriter'>
# csv has header: True, csv dialect: <class 'csv.Sniffer.sniff.<locals>.dialect'>
# open csv for r, use type(csv_reader)=<class '_csv.reader'>
# ['ID', 'Name', 'Age', 'Grade', 'Pass/Fail']
# [1.0, 'Alice', 18.0, 80.5, 'True']
# [2.0, 'Bob', 19.0, 70.0, 'True']
# [3.0, 'Carole', 17.0, 75.0, 'True']
# [4.0, 'David', 18.0, 85.5, 'True']
# Locate Grade of #3 student: 75.0
