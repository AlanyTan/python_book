def main(files: list[str]) -> None:
    int_info = 2
    bool_info = True
    text_info = "Python程序设计\n"
    file_name, open_mode, encoding_type = files[0]
    file_obj = open(file_name, "w+" + open_mode, encoding=encoding_type)
    file_obj.write(f"Line 1, {text_info}")
    file_obj.write(str(int_info))
    file_obj.write("Line 3, string literal.\n")
    file_obj.write(str(bool_info))
    file_obj.write("The End.\n")
    file_obj.close()

    file_name, open_mode, encoding_type = files[1]
    file_obj = open(file_name, "w+" + open_mode, encoding=encoding_type)
    file_obj.write(bytes(f"Line 1, {text_info}",'utf-8'))
    file_obj.write(int_info.to_bytes(4,'little'))
    file_obj.write(bytearray("Line 3, string literal.\n", 'utf-8'))
    file_obj.write(bytes([bool_info]))
    file_obj.write(bytes("The End.\n", 'utf-8'))
    file_obj.close()

if __name__ == "__main__":
    base_name = __file__[:-3]
    file_names = [(base_name + ".data.txt", "t", 'utf-8'),
                  (base_name + ".data.bin", "b", None)]
    main(file_names)
