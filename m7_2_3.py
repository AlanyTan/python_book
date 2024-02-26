def main(file_name: str) -> None:
    int_info = 3
    bool_info = False
    file_obj = open(file_name, 'w+', encoding='utf-8')
    file_obj.write("Line 1, here are some info.\n")
    file_obj.write("Line 2, some more info.\n")
    file_obj.write(f"{int_info}\n")
    file_obj.write(f"{bool_info}\n")
    file_obj.write("The End.\n")
    file_obj.close()


if __name__ == "__main__":
    file_name = __file__ + ".data.txt"
    main(file_name)
