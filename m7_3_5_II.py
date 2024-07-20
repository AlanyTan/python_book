"""Demo .seek of file both text/binary files.

main() function will use .read() read from text file first,
and then read from binary file.

Usage:
    python -m m7_3_5_II

Note: 
    Will first call m7_2_3.main() to create the text and binary files.

Dependencies:
    m7_2_3
"""

import m7_2_3
import io
import os

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
    length_bytes = file_obj.read(m7_2_3.BYTES_FOR_INT)
    length = int.from_bytes(length_bytes, 'little')
    byte_chunk = file_obj.read(length)
    return byte_chunk, file_obj.tell()

def read_from_file(file_name: str, open_mode: str
                   , encoding_type: str = None) -> None:
    """Main func demo seek of both text/binary files.

    Will read a text, an int, a bool, from the files given by files
    and print the length read. Then return to read first item again. 
    
    Args:
        file_names: a list of tuple representing filenames and type of text/binary.

    Returns: 
        None
    """
    file_obj = open(file_name, "r" + open_mode, encoding=encoding_type)
    if 'b' in file_obj.mode:
        data_items = []
        file_pointers = [0]
        while (read_bin_tuple := unpack_b_read(file_obj,
                                                file_pointers[-1]))[0]:
            bytes_read = read_bin_tuple[0]
            data_items.append(bytes_read)
            file_pointers.append(read_bin_tuple[1])
            print(f"# marked binary-file pointer {file_pointers[-1]}")

        text_info_bytes, _ = unpack_b_read(file_obj, file_pointers[0] - file_pointers[-1])
        data_items.append(str(text_info_bytes,'utf-8'))
        print("# Read binary result:", data_items)
    else:
        lines = []
        file_pointers = [0]
        while line := file_obj.readline():
            lines.append(line)
            file_pointers.append(file_obj.tell())
            print(f"# marked text-file pointer {file_pointers[-1]}")          
            
        file_obj.seek(file_pointers[2])
        line = file_obj.readline()
        lines.append(line)
        print("# Read text result:", lines)

    file_obj.close()
    
def main(base_name: str) -> None:
    """Main func calls read_from_file text file then binary file"""
    m7_2_3.write_to_file(base_name + ".data.txt", "t", 'utf-8')
    m7_2_3.write_to_file(base_name + ".data.bin", "b", None)
    print("# reading from text file:")
    read_from_file(base_name + ".data.txt", "t", 'utf-8')
    print("# reading from text file:")
    read_from_file(base_name + ".data.bin", "b", None)


if __name__ == '__main__':
    base_name = __file__[:-3]
    main(base_name)

# reading from text file:
# marked text-file pointer 20
# marked text-file pointer 23
# marked text-file pointer 30
# marked text-file pointer 49
# Read text result: ['Python程序设计\n', '2\n', 'False\n', 'A string literal.\n', 'False\n']
# reading from text file:
# marked binary-file pointer 22
# marked binary-file pointer 30
# marked binary-file pointer 35
# marked binary-file pointer 55
# Read binary result: [b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1', b'\x02\x00\x00\x00', b'\x00', b'a bytes litteral', 'Python程序设计']
