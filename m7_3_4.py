"""Demo .read() method and compare its behavior on text/binary files.

main() function will use .read() read from text file first,
and then read from binary file.

Usage:
    python -m m7_3_4

Note: 
    Will first call m7_2_3.write_to_file() to create the text and binary file.

Dependencies:
    m7_2_3
"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

from m7_2_3 import write_to_file, BYTES_FOR_INT

def unpack_for_b_read(full_content: bytes, idx: int) -> tuple:
    """Func to read content based on the length in the content.

    This function extracts the next object in the full_content from 
    the given idx position.

    Args:
        full_content: a bytes contain the the full content of the bin file.
        idx: the index from whereto start parsing the full_content.

    Returns:
        a tuple of (bytes, total_length_processed), the bytes is the actual
        object that was extracted out of the full_content, the total_length 
        was the length of the object plus the BYTES_FOR_INT bytes used to store
        the prefix where the length of this object is saved.

    Note:
        this function is the opposite of the pack_for_b_write function 
        in the m7_2_3 package.
    """
    idx_content = idx + BYTES_FOR_INT
    length = int.from_bytes(full_content[idx:idx_content], 'little')
    byte_chunk = full_content[idx_content:idx_content+length]
    return byte_chunk, length+BYTES_FOR_INT

def read_from_file(file_name: str, open_mode: str
                   , encoding_type: str = None) -> None:
    """Main func demo read() from both text and binary files.

    Will read a text, an int, a bool, from the files given by files
    and print the length read. 
    
    Args:
        file_names: a list of tuple representing filenames and type of text/binary.

    Returns: 
        None
    """
    file_obj = open(file_name, "r" + open_mode, encoding=encoding_type)
    logger.debug(f"opened {file_name.split('\\')[-1]}, {open_mode=}")
    contents = file_obj.read()
    logger.debug(f"read data: {type(contents)=}")
    if open_mode == 'b':
        idx = 0
        text_info_bytes, length = unpack_for_b_read(contents, idx)
        text_info = str(text_info_bytes, 'utf-8')
        idx += length

        int_info_bytes, length = unpack_for_b_read(contents, idx)
        int_info = int.from_bytes(int_info_bytes,'little')
        idx += length

        bool_info_bytes, length = unpack_for_b_read(contents, idx)
        bool_info = bool(int.from_bytes(bool_info_bytes,'little'))
        print("# Read text:", repr(text_info), ", number:", int_info, 
            ", and boolean:", bool_info)
    else:
        lines = contents.split('\n')
        text_info = lines[0]
        int_info = int(lines[1])
        bool_info = bool(lines[2] == "True")
        print("# Read text:", text_info, ", number:", int_info, 
            ", and boolean:", bool_info)

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

#DEBUG - m7_2_2(m7_2_3.py:33) - write_to_file() called with m7_3_4.data.txt, open_mode='t' 
#DEBUG - m7_2_2(m7_2_3.py:46) - open_mod!='b', processing data as text.
#DEBUG - m7_2_2(m7_2_3.py:53) - write to text file content=['Python程序设计', 2, False, 'A string literal.']
#DEBUG - m7_2_2(m7_2_3.py:33) - write_to_file() called with m7_3_4.data.bin, open_mode='b' 
#DEBUG - m7_2_2(m7_2_3.py:36) - open_mode=='b', processing data as binary.
#DEBUG - m7_2_2(m7_2_3.py:43) - write to binary file content=[bytearray(b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1'), b'\x02\x00\x00\x00', b'\x00', b'a bytes litteral']
#DEBUG - __main__(m7_3_4.py:62) - opened m7_3_4.data.txt, open_mode='t'
#DEBUG - __main__(m7_3_4.py:64) - read data: type(contents)=<class 'str'>
# Read text: Python程序设计 , number: 2 , and boolean: False
#DEBUG - __main__(m7_3_4.py:62) - opened m7_3_4.data.bin, open_mode='b'
#DEBUG - __main__(m7_3_4.py:64) - read data: type(contents)=<class 'bytes'>
# Read text: 'Python程序设计' , number: 2 , and boolean: False
