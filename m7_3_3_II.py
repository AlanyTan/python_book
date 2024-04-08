"""Demo .seek of file both text/binary files.

main() function will use .read() read from text file first,
and then read from binary file.

Usage:
    python -m m7_3_2

Note: 
    Will first call m7_2_3.main() to create the text and binary file.

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
    return byte_chunk, file_obj.tell() #length+m7_2_3.BYTES_FOR_INT

def main(files: list[str]) -> None:
    """Main func demo seek of both text/binary files.

    Will read a text, an int, a bool, from the files given by files
    and print the length read. The return to read first item again. 
    
    Args:
        file_names: a list of tuple representing filenames and type of text/binary.

    Returns: 
        None
    """
    for file_name, open_mode, encoding_type in files:
        file_obj = open(file_name, "r" + open_mode, encoding=encoding_type)
        if 'b' in file_obj.mode:
            data_items = []
            file_pointers = [0]
            while (read_bin_tuple := unpack_b_read(file_obj,
                                                    file_pointers[-1]))[0]:
                bytes_read = read_bin_tuple[0]
                file_pointers.append(read_bin_tuple[1])
                print(f"# {file_pointers[-1]=}")
                data_items.append(bytes_read)

            text_info_bytes, _ = unpack_b_read(file_obj, file_pointers[0])
            data_items.append(str(text_info_bytes,'utf-8'))
            print("# Read binary result:", data_items)
        else:
            lines = []
            file_pointers = [0]
            while line := file_obj.readline():
                file_pointers.append(file_obj.tell())
                print(f"# {file_pointers[-1]=}")          
                lines.append(line)
                
            file_obj.seek(file_pointers[0])
            line = file_obj.readline()
            lines.append(line)
            file_obj.close()
            print("# Read text result:", lines)

        file_obj.close()
    
if __name__ == '__main__':
    base_name = __file__[:-3]
    files = [(base_name + ".data.txt", "t", 'utf-8'),
             (base_name + ".data.bin", "b", None)]
    m7_2_3.main(files)
    main(files)

# file_pointers[-1]=19
# file_pointers[-1]=21
# file_pointers[-1]=27
# Read text result: ['Python程序设计\n', '2\n', 'False\n', 'Python程序设计\n']
# file_pointers[-1]=22
# file_pointers[-1]=30
# file_pointers[-1]=35
# Read binary result: [b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1', b'\x02\x00\x00\x00', b'\x00', 'Python程序设计']
