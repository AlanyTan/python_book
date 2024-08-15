"""Demo .writelines() method and compare its behavior on text/binary files.

main() function will use .write() write to text file first,
and then write a binary file.

Usage:
    python -m m7_2_3
"""

from m7_2_2 import logger, BYTES_FOR_INT, pack_for_b_write

def write_to_file(file_name: str, open_mode: str = None
         , encoding_type: str = None) -> None:
    """func demo write() into both text and binary files.

    Will write a text an int, a bool to the files given by files
    and print the length written. 
    
    Args:
        file_name: name of the file to open and write to
        open_mode: 'b' represents open in binary mode, 't' for text mode
        encoding_type: type of encoding to use when open as text

    Returns: 
        None
    """
    NEWLINE = '\n'
    int_info = 2
    text_info = "Python程序设计"
    bool_info = False

    file_name_no_path = file_name.split('\\')[-1]
    logger.debug(f"write_to_file() called with {file_name_no_path}, {open_mode=} ")
    file_obj = open(file_name, "w+" + open_mode, encoding=encoding_type)
    if open_mode == 'b':
        logger.debug(f"open_mode=='b', processing data as binary.")
        content = [
            bytearray(text_info, 'utf-8'),
            int_info.to_bytes(BYTES_FOR_INT,'little'),
            bytes([bool_info]),
            b'a bytes litteral'            
            ]
        logger.debug(f"write to binary file {content=}")
        file_obj.writelines(map(pack_for_b_write, content))
    else:
        logger.debug(f"open_mod!='b', processing data as text.")
        content = [
            text_info,
            int_info,
            bool_info,
            "A string literal."
            ]
        logger.debug(f"write to text file {content=}")
        file_obj.writelines([f"{c}{NEWLINE}" for c in content])

    file_obj.close()

def main(base_name: str) -> None:
    """Main func call write_to_file as text then bin file"""
    write_to_file(base_name + ".data.txt", "t", 'utf-8')
    write_to_file(base_name + ".data.bin", "b", None)
    

if __name__ == "__main__":
    base_name = __file__[:-3]
    main(base_name)

#DEBUG - m7_2_2(m7_2_3.py:33) - write_to_file() called with m7_2_3.data.txt, open_mode='t' 
#DEBUG - m7_2_2(m7_2_3.py:46) - open_mod!='b', processing data as text.
#DEBUG - m7_2_2(m7_2_3.py:53) - write to text file content=['Python程序设计', 2, False, 'A string literal.']
#DEBUG - m7_2_2(m7_2_3.py:33) - write_to_file() called with m7_2_3.data.bin, open_mode='b' 
#DEBUG - m7_2_2(m7_2_3.py:36) - open_mode=='b', processing data as binary.
#DEBUG - m7_2_2(m7_2_3.py:43) - write to binary file content=[bytearray(b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1'), b'\x02\x00\x00\x00', b'\x00', b'a bytes litteral']
