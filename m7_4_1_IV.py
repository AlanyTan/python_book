"""Demo csv.Sniffer() ability to guess csv dialect.

Usage:
    python -m m7_4_1_IV

Note:
    depends on m7_4_1_III, which in turn depends on m7_4_1_I.
"""
import csv
from os.path import basename
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
    logger.debug("created %s as excel dialect csv.", basename(file_name))
    csv_file_obj.close()

    csv_file_obj = open(file_name, "r", newline='', encoding='utf-8')
    csv_beginning = csv_file_obj.read(1024)
    csv_file_obj.seek(0)
    csv_has_header = csv.Sniffer().has_header(csv_beginning)
    csv_dialect = csv.Sniffer().sniff(csv_beginning)
    logger.debug("sniffed %s chars and guessed as %r, has_header=%s",
                 len(csv_beginning), csv_dialect.__dict__, csv_has_header)
    csv_reader = csv.reader(csv_file_obj, dialect=csv_dialect,
                            quoting=csv.QUOTE_NONNUMERIC)
    data_table = []
    for row in csv_reader:
        print("#", row)
        data_table.append(row)

    print(f"# Retrieve of #3 student: {data_table[2 + csv_has_header]}")

    csv_file_obj.close()


if __name__ == '__main__':
    namebase = __file__[:-3]
    filename = (namebase + ".data.csv")
    main(filename)

#DEBUG - __main__(m7_4_1_IV.py:27) - created m7_4_1_IV.data.csv as excel dialect csv.
#DEBUG - __main__(m7_4_1_IV.py:35) - sniffed 168 chars and guessed as mappingproxy({'__module__': 'csv', '_name': 'sniffed', 'lineterminator': '\r\n', 'quoting': 0, '__doc__': None, 'doublequote': False, 'delimiter': ',', 'quotechar': '"', 'skipinitialspace': False}) with header=True
# ['ID', 'Name', 'Age', 'Grade', 'Pass/Fail']
# [1.0, 'Zhang, Alice', 18.0, 80.5, 'True']
# [2.0, 'Yusuf, Bob', 19.0, 70.0, 'True']
# [3.0, 'Xanders, Carole', 17.0, 55.0, 'False']
# [4.0, 'West, David', 18.0, 85.5, 'True']
# Retrieve of #3 student: [3.0, 'Xanders, Carole', 17.0, 55.0, 'False']
