"""Demo csv.Sniffer() ability to guess csv dialect.

Usage:
    python -m m7_4_1_IV

Note:
    depends on m7_4_1_III, which in turn depends on m7_4_1_I.
"""
import csv
import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

import m7_4_1_II

def main(file_name: str) -> None:
    """main func showing csv.Sniffer() guess header and dialect.
    
    Args:
        file_name: string representing filename to use.
    """
    csv_file_obj = open(file_name, "w", newline='', encoding='utf-8')
    m7_4_1_II.write_csv(csv_file_obj, m7_4_1_II.SAMPLE_DATA)
    logger.debug(f"{file_name.split('\\')[-1]} created as excel dialect.")
    csv_file_obj.close()

    csv_file_obj = open(file_name, "r", newline='', encoding='utf-8')
    csv_beginning = csv_file_obj.read(1024)
    csv_file_obj.seek(0)
    csv_has_header = csv.Sniffer().has_header(csv_beginning)
    csv_dialect = csv.Sniffer().sniff(csv_beginning)
    logger.debug(f"sniffed {len(csv_beginning)} chars and guessed: "
                 f"{csv_has_header=},{csv_dialect._name=}")
    csv_reader = csv.reader(csv_file_obj, dialect=csv_dialect,
                            quoting=csv.QUOTE_NONNUMERIC)
    data_table = []
    for row in csv_reader:
        print("#", row)
        data_table.append(row)
    
    print(f"# Retrieve of #3 student: {data_table[2+csv_has_header]}")
        
    csv_file_obj.close()

if __name__ == '__main__':
    base_name = __file__[:-3]
    file_name = (base_name + ".data.csv")
    main(file_name)

#DEBUG - m7_4_1_II(m7_4_1_II.py:32) - write_csv() called with: m7_4_1_IV.data.csv(w), [['ID', 'Name', 'Age', 'Grade', 'Pass/Fail'], [1, 'Zhang, Alice', 18, 80.5, True...
#DEBUG - __main__(m7_4_1_IV.py:25) - m7_4_1_IV.data.csv created as excel dialect.
#DEBUG - __main__(m7_4_1_IV.py:33) - sniffed 168 and guessed: csv_has_header=True,csv_dialect._name='sniffed'
# ['ID', 'Name', 'Age', 'Grade', 'Pass/Fail']
# [1.0, 'Zhang, Alice', 18.0, 80.5, 'True']
# [2.0, 'Yusuf, Bob', 19.0, 70.0, 'True']
# [3.0, 'Xanders, Carole', 17.0, 55.0, 'False']
# [4.0, 'West, David', 18.0, 85.5, 'True']
# Retrieve of #3 student: [3.0, 'Xanders, Carole', 17.0, 55.0, 'False']
