"""Demo .writelines() method and compare its behavior on text/binary files.

main() function will use .write() write to text file first,
and then write a binary file.

Usage:
    python -m m7_2_3
"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)
from m7_2_2 import BYTES_FOR_INT, pack_for_b_write


def write_to_file(file_name: str, open_mode: str = '',
                  encoding_type: str | None = None) -> None:
    """func demo writelines() into both text and binary files.

    Will write a list containing a text, an int, a bool to the file_name file. 

    Args:
        file_name: name of the file to open and write to
        open_mode: 'b' represents open in binary mode, 't' for text mode
        encoding_type: type of encoding to use when open as text
    """
    NEWLINE = '\n'
    int_info = 2
    text_info = "Python程序设计"
    bool_info = False
    short_file_name = "..." + file_name[-15:]
    logger.debug("entering write_to_file(%s, %s, %s)...",
                 short_file_name, open_mode, encoding_type)
    file_obj = open(file_name, "w+" + open_mode, encoding=encoding_type)
    if open_mode == 'b':
        logger.debug("processing data as binary.")
        content = [
            bytearray(text_info, 'utf-8'),
            int_info.to_bytes(BYTES_FOR_INT, 'little'),
            bytes([bool_info]),
            b'a bytes litteral'
        ]
        logger.debug("writelines() to binary file: %s", content)
        file_obj.writelines(map(pack_for_b_write, content))
    else:
        logger.debug("processing data as text.")
        content = [
            text_info,
            int_info,
            bool_info,
            "A string literal."
        ]
        logger.debug("writelines() to text file: %s", content)
        file_obj.writelines([f"{c}{NEWLINE}" for c in content])

    logger.debug("file %s closed.", {short_file_name})
    file_obj.close()


def main(name_base: str) -> None:
    """Main func demo writelines() into text file.

    Will call write_to_file to write() an int, a bool, a str variable and 
    a str literal to a text file and a binary file.

    Args:
        base_name: string representing file name trunk,
                    will add .txt or .bin to indicate text or binary files.

    Returns: 
        None
    """
    write_to_file(name_base + ".data.txt", "t", 'utf-8')
    write_to_file(name_base + ".data.bin", "b", None)


if __name__ == "__main__":
    namebase = __file__[:-3]
    main(namebase)

#DEBUG - __main__(m7_2_3.py:33) - entering write_to_file(...m7_2_3.data.txt, t, utf-8)...
#DEBUG - __main__(m7_2_3.py:47) - processing data as text.
#DEBUG - __main__(m7_2_3.py:54) - writelines() to text file: ['Python程序设计', 2, False, 'A string literal.']
#DEBUG - __main__(m7_2_3.py:57) - file {'...m7_2_3.data.txt'} closed.
#DEBUG - __main__(m7_2_3.py:33) - entering write_to_file(...m7_2_3.data.bin, b, None)...
#DEBUG - __main__(m7_2_3.py:37) - processing data as binary.
#DEBUG - __main__(m7_2_3.py:44) - writelines() to binary file: [bytearray(b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1'), b'\x02\x00\x00\x00', b'\x00', b'a bytes litteral']
#DEBUG - m7_2_2(m7_2_2.py:39) - ..pack_for_write: bytearray(b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1') is 18 bytes
#DEBUG - m7_2_2(m7_2_2.py:39) - ..pack_for_write: b'\x02\x00\x00\x00' is 4 bytes
#DEBUG - m7_2_2(m7_2_2.py:39) - ..pack_for_write: b'\x00' is 1 bytes
#DEBUG - m7_2_2(m7_2_2.py:39) - ..pack_for_write: b'a bytes litteral' is 16 bytes
#DEBUG - __main__(m7_2_3.py:57) - file {'...m7_2_3.data.bin'} closed.
