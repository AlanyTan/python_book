"""Demo .read() method and compare its behavior on text/binary files.

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
    idx_content = idx + m7_2_3.BYTES_FOR_INT
    length = int.from_bytes(full_content[idx:idx_content], 'little')
    byte_chunk = full_content[idx_content:idx_content+length]
    return byte_chunk, length+m7_2_3.BYTES_FOR_INT

def main(files: list[str]) -> None:
    """Main func demo read() from both text and binary files.

    Will read a text, an int, a bool, from the files given by files
    and print the length read. 
    
    Args:
        file_names: a list of tuple representing filenames and type of text/binary.

    Returns: 
        None
    """
    for file_name, open_mode, encoding_type in files:
        file_obj = open(file_name, "r" + open_mode, encoding=encoding_type)
        contents = file_obj.read()
        print(f"# {type(contents)=}")
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
            file_obj.close()
            print("# Read text:", text_info, ", number:", int_info, 
                ", and boolean:", bool_info)

    file_obj.close()
    
if __name__ == '__main__':
    base_name = __file__[:-3]
    files = [(base_name + ".data.txt", "t", 'utf-8'),
             (base_name + ".data.bin", "b", None)]
    m7_2_3.main(files)
    main(files)

# type(contents)=<class 'str'>
# Read text: Python程序设计 , number: 2 , and boolean: False
# type(contents)=<class 'bytes'>
# Read text: 'Python程序设计' , number: 2 , and boolean: False
