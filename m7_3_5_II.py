"""Demo .seek of file both text/binary files.

main() function will use .read() read from text file first,
and then read from binary file.

Usage:
    python -m m7_3_5_II

Note: 
    Will first call m7_2_3.write_to_file() to create the text and binary files.

Dependencies:
    m7_2_3
"""

import io
import os
import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

from m7_2_3 import write_to_file, BYTES_FOR_INT


def unpack_b_read(file_obj: io.BufferedReader, idx: int) -> tuple:
    """Func to read file_obj content according to idx given

    This function extracts the next object directly from 
    the file_obj start from the given idx position.

    Args:
        file_obj: file obj that had already been opened.
        idx: the index from whereto start reading.

    Returns:
        a tuple of (bytes, total_length_processed), the bytes is the actual
        object that was read out of the file_obj, the total_length 
        was the length of the object plus the BYTES_FOR_INT bytes used to store
        the prefix where the length of this object is saved.

    Note:
        this function reads from file directly, do not rely on parent 
        function reading the contents and pass it to this func.
    """
    if idx < 0:
        file_obj.seek(idx, os.SEEK_END)
    else:
        file_obj.seek(idx)
    length_bytes = file_obj.read(BYTES_FOR_INT)
    length = int.from_bytes(length_bytes, 'little')
    byte_chunk = file_obj.read(length)
    logger.debug(" unpack_b_read() from %d read: %r, marked file pointer %d",
                 idx, byte_chunk, file_obj.tell())
    return byte_chunk, file_obj.tell()


def read_from_file(file_name: str, open_mode: str, encoding_type: str = None) -> None:
    """Main func demo seek of both text/binary files.

    Will read a text, an int, a bool, from the files given by files
    and print the length read. Then return to read first item again. 

    Args:
        file_names: a list of tuple representing filenames & type of text/binary.

    Returns: 
        None
    """
    file_obj = open(file_name, "r" + open_mode, encoding=encoding_type)
    logger.debug("opened %s, open_mode=%s", file_name[-15:], file_obj.mode)
    if 'b' in file_obj.mode:
        data_items = []
        file_pointers = [0]
        while (read_bin_tuple := unpack_b_read(file_obj,
                                               file_pointers[-1]))[0]:
            bytes_read = read_bin_tuple[0]
            data_items.append(bytes_read)
            file_pointers.append(read_bin_tuple[1])

        text_info_bytes, _ = unpack_b_read(
            file_obj, file_pointers[0] - file_pointers[-1])
        data_items.append(str(text_info_bytes, 'utf-8'))
        print("# Read binary result:", data_items)
    else:
        lines = []
        file_pointers = [0]
        while line := file_obj.readline():
            lines.append(line)
            file_pointers.append(file_obj.tell())
            logger.debug(" read_from_file() read %r, marked file pointer= %d",
                         line, file_pointers[-1])

        file_obj.seek(file_pointers[2])
        line = file_obj.readline()
        logger.debug(" read_from_file() read %r, marked file pointer= %d",
                     line, file_pointers[-1])
        bool_info = line.strip() == 'True'
        lines.append(bool_info)
        print("# Read text result:", lines)

    file_obj.close()


def main(name_base: str) -> None:
    """Main func calls read_from_file text file then binary file"""
    write_to_file(name_base + ".data.txt", "t", 'utf-8')
    write_to_file(name_base + ".data.bin", "b", None)
    read_from_file(name_base + ".data.txt", "t", 'utf-8')
    read_from_file(name_base + ".data.bin", "b", None)


if __name__ == '__main__':
    namebase = __file__[:-3]
    main(namebase)

#DEBUG - m7_2_3(m7_2_3.py:33) - entering write_to_file(...3_5_II.data.txt, t, utf-8)...
#DEBUG - m7_2_3(m7_2_3.py:47) - processing data as text.
#DEBUG - m7_2_3(m7_2_3.py:54) - writelines() to text file: ['Python程序设计', 2, False, 'A string literal.']
#DEBUG - m7_2_3(m7_2_3.py:57) - file {'...3_5_II.data.txt'} closed.
#DEBUG - m7_2_3(m7_2_3.py:33) - entering write_to_file(...3_5_II.data.bin, b, None)...
#DEBUG - m7_2_3(m7_2_3.py:37) - processing data as binary.
#DEBUG - m7_2_3(m7_2_3.py:44) - writelines() to binary file: [bytearray(b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1'), b'\x02\x00\x00\x00', b'\x00', b'a bytes litteral']
#DEBUG - m7_2_2(m7_2_2.py:39) - ..pack_for_write: bytearray(b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1') is 18 bytes
#DEBUG - m7_2_2(m7_2_2.py:39) - ..pack_for_write: b'\x02\x00\x00\x00' is 4 bytes
#DEBUG - m7_2_2(m7_2_2.py:39) - ..pack_for_write: b'\x00' is 1 bytes
#DEBUG - m7_2_2(m7_2_2.py:39) - ..pack_for_write: b'a bytes litteral' is 16 bytes
#DEBUG - m7_2_3(m7_2_3.py:57) - file {'...3_5_II.data.bin'} closed.
#DEBUG - __main__(m7_3_5_II.py:71) - opened 3_5_II.data.txt, open_mode=rt
#DEBUG - __main__(m7_3_5_II.py:91) -  read_from_file() read 'Python程序设计\n', marked file pointer= 19
#DEBUG - __main__(m7_3_5_II.py:91) -  read_from_file() read '2\n', marked file pointer= 21
#DEBUG - __main__(m7_3_5_II.py:91) -  read_from_file() read 'False\n', marked file pointer= 27
#DEBUG - __main__(m7_3_5_II.py:91) -  read_from_file() read 'A string literal.\n', marked file pointer= 45
#DEBUG - __main__(m7_3_5_II.py:96) -  read_from_file() read 'False\n', marked file pointer= 45
# Read text result: ['Python程序设计\n', '2\n', 'False\n', 'A string literal.\n', False]
#DEBUG - __main__(m7_3_5_II.py:71) - opened 3_5_II.data.bin, open_mode=rb
#DEBUG - __main__(m7_3_5_II.py:53) -  unpack_b_read() from 0 read: b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1', marked file pointer 22
#DEBUG - __main__(m7_3_5_II.py:53) -  unpack_b_read() from 22 read: b'\x02\x00\x00\x00', marked file pointer 30
#DEBUG - __main__(m7_3_5_II.py:53) -  unpack_b_read() from 30 read: b'\x00', marked file pointer 35
#DEBUG - __main__(m7_3_5_II.py:53) -  unpack_b_read() from 35 read: b'a bytes litteral', marked file pointer 55
#DEBUG - __main__(m7_3_5_II.py:53) -  unpack_b_read() from 55 read: b'', marked file pointer 55
#DEBUG - __main__(m7_3_5_II.py:53) -  unpack_b_read() from -55 read: b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1', marked file pointer 22
# Read binary result: [b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1', b'\x02\x00\x00\x00', b'\x00', b'a bytes litteral', 'Python程序设计']
