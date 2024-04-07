"""Demo .write() method and compare its behavior on text/binary files.

main() function will use .write() write to text file first,
and then write a binary file.
"""
BYTES_FOR_INT = 4

def pack_for_b_w(bytestream: bytes|bytearray) -> bytes:
    """Func to add length of bytes in front of the bytestream itself.

    This function can be used to convert a bytestream to a structure 
    with 2 bytes of length as prefix of it. This length can be used 
    during reading to know how many bytes belong to this bytestream 
    and where does the next object starts in the binary file.

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

def main(files: list[str]) -> None:
    """Main func demo write() into text file both text and binary.

    Will write an int, a bool, a text to the files given by files
    and print the length written. 
    
    Args:
        file_names: a list of string representing filenames and type of text/binary.

    Returns: 
        None
    """
    int_info = 2
    bool_info = False
    text_info = "Python程序设计"
    newline = '\n'


    for file_name, open_mode, encoding_type in files:
        file_obj = open(file_name, "w+" + open_mode, encoding=encoding_type)
        if open_mode == 'b':
            print("# .write() str to bin file returned:",
                  file_obj.write(pack_for_b_w(bytes(text_info, 'utf-8'))))
            print("# .write() int to bin file returned:",
                  file_obj.write(pack_for_b_w(
                            int_info.to_bytes(BYTES_FOR_INT,'little'))))
            print("# .write() bool to bin file returned:",
                  file_obj.write(pack_for_b_w(bytearray([bool_info]))))
        else:
            print("# .write() str to text file returned:",
                  file_obj.write(text_info+newline))
            print("# .write() int to text file returned:",
                  file_obj.write(str(int_info)+newline))
            print("# .write() bool to text file returned:",
                  file_obj.write(str(bool_info)+newline))

        file_obj.close()

if __name__ == "__main__":
    base_name = __file__[:-3]
    file_names = [(base_name + ".data.txt", "t", 'utf-8'),
                  (base_name + ".data.bin", "b", None)]
    main(file_names)

# .write() str to text file returned: 11
# .write() int to text file returned: 2
# .write() bool to text file returned: 6
# .write() str to bin file returned: 22
# .write() int to bin file returned: 8
# .write() bool to bin file returned: 5
