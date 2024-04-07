def main(file_name: str) -> None:
    """Main func demo writelines() into text file.

    Will first prepare a list of strings.
    The open file_name for write (default t|b so text), 
    create if not yet exist, truncate the file if already exist.
    Next, writelines() the list into the opened file_obj.
    Last, close the file_obj.
    
    Args:
        file_name: string representing file name to create and open.

    Returns: 
        None
    """
    int_info = 2
    bool_info = True
    text_info = "text content containing 2 & True"
    content = [
        f"{text_info}\n",
        f"{int_info}\n",
        f"{bool_info}\n",
        "A string liternal.\n"
    ]
    file_obj = open(file_name, 'w+', encoding='utf-8')
    file_obj.writelines(content)
    file_obj.close()


if __name__ == "__main__":
    base_name = __file__[:-3]
    file_name = base_name + ".data.txt"
    main(file_name)
