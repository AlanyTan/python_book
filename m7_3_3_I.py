import m7_2_3
import io
import os
def unpack_for_b_w(file_obj: io.BufferedReader, idx: int) -> tuple:
    if idx < 0: 
        file_obj.seek(idx, os.SEEK_END)
    else:
        file_obj.seek(idx)
    length_bytes = file_obj.read(2)
    length = int.from_bytes(length_bytes, 'little')
    byte_chunk = file_obj.read(length)
    return byte_chunk, length+2

def main(files: list[str]) -> None:
    file_name, open_mode, encoding_type = files[0]
    file_obj = open(file_name, "r" + open_mode, encoding=encoding_type)
    prev_file_pointer = file_pointer = 0
    lines = []
    while line := file_obj.readline():
        prev_file_pointer = file_pointer
        file_pointer = file_obj.tell()
        print(f"# {file_pointer=}")          
        lines.append(line)
        
    file_obj.seek(prev_file_pointer)
    line = bool(file_obj.readline())
    lines.append(line)
    file_obj.close()
    print("# Read text result:", lines)
    file_obj.close()

    file_name, open_mode, encoding_type = files[1]
    file_obj = open(file_name, "r" + open_mode, encoding=encoding_type)

    data_items = []
    file_pointer = 0
    while (read_bin_tuple := unpack_for_b_w(file_obj, file_pointer))[0]:
        bytes_read = read_bin_tuple[0]
        length = read_bin_tuple[1]
        file_pointer += length
        print(f"# {file_pointer=}")
        data_items.append(bytes_read)

    bool_info_bytes, length = unpack_for_b_w(file_obj, -length)
    data_items.append(bool(bool_info_bytes))
    print("# Read binary result:", data_items)
    file_obj.close()
    
if __name__ == '__main__':
    base_name = __file__[:-3]
    files = [(base_name + ".data.txt", "t", 'utf-8'),
             (base_name + ".data.bin", "b", None)]
    m7_2_3.main(files)
    main(files)

# file_pointer=19
# file_pointer=21
# file_pointer=39
# file_pointer=44
# Read text result: ['Python程序设计\n', '2\n', 'A string literal.\n', 'True\n', True]
# file_pointer=20
# file_pointer=26
# file_pointer=45
# file_pointer=48
# Read binary result: [b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1', b'\x02\x00\x00\x00', b'Astring literal.\n', b'\x01', True]
