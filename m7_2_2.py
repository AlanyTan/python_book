def main(file_name: str) -> None:
    int_info = 2
    bool_info = True
    text_info = "str variable text content"
    content = [
        f"{text_info}.\n",
        f"{int_info}\n",
        "A string liternal.\n",
        f"{bool_info}\n"
    ]
    file_obj = open(file_name, 'w+', encoding='utf-8')
    file_obj.writelines(content)
    file_obj.close()


if __name__ == "__main__":
    base_name = __file__[:-3]
    file_name = base_name + ".data.txt"
    main(file_name)
