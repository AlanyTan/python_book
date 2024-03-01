import m7_2_3

def unpack_for_b_w(full_content: bytes, idx: int) -> tuple:
    length = int.from_bytes(full_content[idx:idx+2], 'little')
    idx_content = idx + 2
    byte_chunk = full_content[idx_content:idx_content+length]
    return byte_chunk, length+2

def main(files: list[str]) -> None:
    file_name, open_mode, encoding_type = files[0]
    file_obj = open(file_name, "r" + open_mode, encoding=encoding_type)
    content = file_obj.read()
    print(f"# {type(content)=}")
    lines = content.split('\n')
    text_info = lines[0]
    int_info = int(lines[1])
    text_literal = lines[2]
    bool_info = bool(lines[2].startswith("True"))
    file_obj.close()
    print("# Read text:", text_info, ", number:", int_info, 
          ", text literal:", text_literal, ", and boolean:", bool_info)
    file_obj.close()

    file_name, open_mode, encoding_type = files[1]
    file_obj = open(file_name, "r" + open_mode, encoding=encoding_type)
    content = file_obj.read()
    print(f"# {type(content)=}")

    idx = 0
    text_info_bytes, length = unpack_for_b_w(content, idx)
    text_info = str(text_info_bytes, 'utf-8')
    idx += length

    int_info_bytes, length = unpack_for_b_w(content, idx)
    int_info = int.from_bytes(int_info_bytes,'little')
    idx += length

    text_literal_bytes, length = unpack_for_b_w(content, idx)
    text_literal = str(text_literal_bytes, 'utf-8')
    idx += length

    bool_info_bytes, length = unpack_for_b_w(content, idx)
    bool_info = bool(bool_info_bytes)
    print("# Read text:", repr(text_info), ", number:", int_info, 
          ", text literal:", repr(text_literal),", and boolean:", bool_info)
    file_obj.close()
    
if __name__ == '__main__':
    base_name = __file__[:-3]
    files = [(base_name + ".data.txt", "t", 'utf-8'),
             (base_name + ".data.bin", "b", None)]
    m7_2_3.main(files)
    main(files)

# type(content)=<class 'str'>
# Read text: Python程序设计 , number: 2 , text literal: Line 3, string literal. , and boolean: False
# type(content)=<class 'bytes'>
# Read text: 'Line 1, Python程序设计' , number: 2 , text literal: 'Line 3, string literal.\n' , and boolean: True