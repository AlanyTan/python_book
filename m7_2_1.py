def main(file_name: str) -> None:
    int_info = 2
    bool_info = True
    text_info = "text like this"
    file_obj = open(file_name, 'w+', encoding='utf-8')
    print("Saving", text_info, ", number", int_info, ", and boolean", 
          bool_info, file=file_obj)
    print(f"into file {file_name}",
           file=file_obj)
    file_obj.close()


if __name__ == "__main__":
    base_name = __file__[:-3]
    file_name = base_name + ".data.txt"
    main(file_name)
