"""Demo .write() method and compare its behavior on text/binary files.

main() function will use .write() write to text file first,
and then write a binary file.

Usage:
    python -m m7_2_2
"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

BYTES_FOR_INT = 4


def pack_for_b_write(bytestream: bytes | bytearray) -> bytes:
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
        i.e. when BYTES_FOR_INT=4, this func can handle 2^32-1 bytes stream.
    """
    length = len(bytestream)
    logger.debug("..pack_for_write: %s is %s bytes", bytestream, length)
    return length.to_bytes(BYTES_FOR_INT, 'little') + bytestream


def write_to_file(file_name: str, open_mode: str = '',
                  encoding_type: str | None = None) -> None:
    """Main func demo write() into both text and binary files.

    Write a text, an int, a bool to the files and return chars/bytes written 

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

    short_file_name = "..." + file_name[-15:]
    logger.debug("entering write_to_file(%s, %s, %s)...",
                 short_file_name, open_mode, encoding_type)

    file_obj = open(file_name, "w+" + open_mode, encoding=encoding_type)
    if open_mode == 'b':
        logger.debug("processing data as binary.")
        print("# .write() str to bin file returned:",
              file_obj.write(pack_for_b_write(bytes(text_info, 'utf-8'))))
        print("# .write() int to bin file returned:",
              file_obj.write(pack_for_b_write(
                  int_info.to_bytes(BYTES_FOR_INT, 'little'))))
        print("# .write() bool to bin file returned:",
              file_obj.write(pack_for_b_write(bytearray([bool_info]))))
    else:
        logger.debug("processing data as text.")
        print("# .write() str to text file returned:",
              file_obj.write(text_info + NEWLINE))
        print("# .write() int to text file returned:",
              file_obj.write(str(int_info) + NEWLINE))
        print("# .write() bool to text file returned:",
              file_obj.write(str(bool_info) + NEWLINE))
    logger.debug("file %s closed.", {short_file_name})
    file_obj.close()


def main(name_base: str) -> None:
    """Main func demo write() into text file.

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

#DEBUG - __main__(m7_2_2.py:63) - entering write_to_file(...m7_2_2.data.txt, t, utf-8)...
#DEBUG - __main__(m7_2_2.py:77) - processing data as text.
# .write() str to text file returned: 11
# .write() int to text file returned: 2
# .write() bool to text file returned: 6
#DEBUG - __main__(m7_2_2.py:84) - file {'...m7_2_2.data.txt'} closed.
#DEBUG - __main__(m7_2_2.py:63) - entering write_to_file(...m7_2_2.data.bin, b, None)...
#DEBUG - __main__(m7_2_2.py:68) - processing data as binary.
#DEBUG - __main__(m7_2_2.py:39) - ..pack_for_write: b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1' is 18 bytes
# .write() str to bin file returned: 22
#DEBUG - __main__(m7_2_2.py:39) - ..pack_for_write: b'\x02\x00\x00\x00' is 4 bytes
# .write() int to bin file returned: 8
#DEBUG - __main__(m7_2_2.py:39) - ..pack_for_write: bytearray(b'\x00') is 1 bytes
# .write() bool to bin file returned: 5
#DEBUG - __main__(m7_2_2.py:84) - file {'...m7_2_2.data.bin'} closed.
