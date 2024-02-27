def main(file_name: str) -> None:
    int_info = 2
    bool_info = True
    text_info = "text like this"
    content = [
        f"Line 1, {text_info}.\n",
        f"{int_info}\n",
        "Line 3, string liternal.\n",
        f"{bool_info}\n",
        "The End.\n"
    ]
    file_obj = open(file_name, 'w+', encoding='utf-8')
    file_obj.writelines(content)
    file_obj.close()


if __name__ == "__main__":
    base_name = __file__[:-3]
    file_name = base_name + ".data.txt"
    main(file_name)
