def main(file_name: str) -> None:
    int_info = 3
    bool_info = False
    content = [
        "Line 1, here are some info.\n",
        "Line 2, some more info.\n",
        f"{int_info}\n",
        f"{False}\n",
        "The End.\n"
    ]
    file_obj = open(file_name, 'w+', encoding='utf-8')
    file_obj.writelines(content)
    file_obj.close()


if __name__ == "__main__":
    file_name = __file__ + ".data.txt"
    main(file_name)
