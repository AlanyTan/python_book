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
    logger.debug(f" unpack_b_read() from {idx} read: {byte_chunk=}, "
             f"marked binary-file pointer {file_obj.tell()}")
    return byte_chunk, file_obj.tell()

def read_from_file(file_name: str, open_mode: str
                   , encoding_type: str = None) -> None:
    """Main func demo seek of both text/binary files.

    Will read a text, an int, a bool, from the files given by files
    and print the length read. Then return to read first item again. 
    
    Args:
        file_names: a list of tuple representing filenames & type of text/binary.

    Returns: 
        None
    """
    file_obj = open(file_name, "r" + open_mode, encoding=encoding_type)
    logger.debug(f"opened {file_name.split('\\')[-1]}, {file_obj.mode=}")
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
        data_items.append(str(text_info_bytes,'utf-8'))
        print("# Read binary result:", data_items)
    else:
        lines = []
        file_pointers = [0]
        while line := file_obj.readline():
            lines.append(line)
            file_pointers.append(file_obj.tell())
            logger.debug(f" read_from_file() read {line=}, "
                         f"marked text-file pointer {file_pointers[-1]}")
            
        file_obj.seek(file_pointers[2])
        line = file_obj.readline()
        logger.debug(f" read_from_file() read {line=}, "
                     f"marked text-file pointer {file_pointers[-1]}")
        bool_info = line.strip() == 'True'
        lines.append(bool_info)
        print("# Read text result:", lines)

    file_obj.close()
    
def main(base_name: str) -> None:
    """Main func calls read_from_file text file then binary file"""
    write_to_file(base_name + ".data.txt", "t", 'utf-8')
    write_to_file(base_name + ".data.bin", "b", None)
    read_from_file(base_name + ".data.txt", "t", 'utf-8')
    read_from_file(base_name + ".data.bin", "b", None)


if __name__ == '__main__':
    base_name = __file__[:-3]
    main(base_name)

#DEBUG - m7_2_2(m7_2_3.py:33) - write_to_file() called with m7_3_5_II.data.txt, open_mode='t' 
#DEBUG - m7_2_2(m7_2_3.py:46) - open_mod!='b', processing data as text.
#DEBUG - m7_2_2(m7_2_3.py:53) - write to text file content=['Python程序设计', 2, False, 'A string literal.']
#DEBUG - m7_2_2(m7_2_3.py:33) - write_to_file() called with m7_3_5_II.data.bin, open_mode='b' 
#DEBUG - m7_2_2(m7_2_3.py:36) - open_mode=='b', processing data as binary.
#DEBUG - m7_2_2(m7_2_3.py:43) - write to binary file content=[bytearray(b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1'), b'\x02\x00\x00\x00', b'\x00', b'a bytes litteral']
#DEBUG - __main__(m7_3_5_II.py:70) - opened m7_3_5_II.data.txt, file_obj.mode='rt'
#DEBUG - __main__(m7_3_5_II.py:90) -  read_from_file() read line='Python程序设计\n', marked text-file pointer 20
#DEBUG - __main__(m7_3_5_II.py:90) -  read_from_file() read line='2\n', marked text-file pointer 23
#DEBUG - __main__(m7_3_5_II.py:90) -  read_from_file() read line='False\n', marked text-file pointer 30
#DEBUG - __main__(m7_3_5_II.py:90) -  read_from_file() read line='A string literal.\n', marked text-file pointer 49
#DEBUG - __main__(m7_3_5_II.py:95) -  read_from_file() read line='False\n', marked text-file pointer 49
# Read text result: ['Python程序设计\n', '2\n', 'False\n', 'A string literal.\n', False]
#DEBUG - __main__(m7_3_5_II.py:70) - opened m7_3_5_II.data.bin, file_obj.mode='rb'
#DEBUG - __main__(m7_3_5_II.py:52) -  unpack_b_read() from 0 read: byte_chunk=b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1', marked binary-file pointer 22
#DEBUG - __main__(m7_3_5_II.py:52) -  unpack_b_read() from 22 read: byte_chunk=b'\x02\x00\x00\x00', marked binary-file pointer 30
#DEBUG - __main__(m7_3_5_II.py:52) -  unpack_b_read() from 30 read: byte_chunk=b'\x00', marked binary-file pointer 35
#DEBUG - __main__(m7_3_5_II.py:52) -  unpack_b_read() from 35 read: byte_chunk=b'a bytes litteral', marked binary-file pointer 55
#DEBUG - __main__(m7_3_5_II.py:52) -  unpack_b_read() from 55 read: byte_chunk=b'', marked binary-file pointer 55
#DEBUG - __main__(m7_3_5_II.py:52) -  unpack_b_read() from -55 read: byte_chunk=b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1', marked binary-file pointer 22
# Read binary result: [b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1', b'\x02\x00\x00\x00', b'\x00', b'a bytes litteral', 'Python程序设计']
