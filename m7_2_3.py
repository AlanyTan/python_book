"""Demo .writelines() method and compare its behavior on text/binary files.

main() function will use .write() write to text file first,
and then write a binary file.

Usage:
    python -m m7_2_3
"""
BYTES_FOR_INT = 4

def pack_for_b_write(bytestream: bytes|bytearray) -> bytes:
    """Func to add length of bytes in front of the bytestream itself.

    This function can be used to convert a bytestream to a structure 
    with BYTES_FOR_INT bytes of length as prefix of it. This length
    can be used     during reading to know how many bytes belong to
    this bytestream and where does the next object starts in the
    binary file.

    Args:
        bytestream: a bytes or bytearray containing info to be saved.

    Returns:
        a bytes obj with the length added as prefix of the incoming bytes.

    Note:
        length of bytestream is added as BYTES_FOR_INT bytes, so the length
        of the bytestream this function can handle is limited by this CONSTANT.
        i.e. when BYTES_FOR_INT=4, the largest bytes this func can handle 
        is 2^32-1 long.
    """
    length = len(bytestream)
    return length.to_bytes(BYTES_FOR_INT, 'little') + bytestream

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


    file_obj = open(file_name, "w+" + open_mode, encoding=encoding_type)
    if open_mode == 'b':
        content = [
            bytearray(text_info, 'utf-8'),
            int_info.to_bytes(BYTES_FOR_INT,'little'),
            bytes([bool_info]),
            b'a bytes litteral'            
            ]
        file_obj.writelines(map(pack_for_b_write, content))
    else:
        content = [
            text_info,
            int_info,
            bool_info,
            "A string literal."
            ]
        file_obj.writelines([f"{c}{NEWLINE}" for c in content])

    file_obj.close()

def main(base_name: str) -> None:
    """Main func call write_to_file as text then bin file"""
    write_to_file(base_name + ".data.txt", "t", 'utf-8')
    write_to_file(base_name + ".data.bin", "b", None)
    

if __name__ == "__main__":
    base_name = __file__[:-3]
    main(base_name)
