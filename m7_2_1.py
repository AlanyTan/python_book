"""print() info into textfile"""
def main(file_name: str) -> None:
    """Main func demo print() into text file.

    Will print an int, a bool, a str variable and a str literal to
    a text file opened using file_name given.
    
    Args:
        file_name: string representing file name to create and open.

    Returns: 
        None
    """
    int_info = 2
    bool_info = True
    text_info = "text content containing 2 & True"
    file_obj = open(file_name, 'w+', encoding='utf-8')
    print("Saving text:", text_info, file=file_obj)
    print("Saving number:", int_info, file=file_obj)
    print("Saving boolean:", bool_info, file=file_obj)
    print(f"into file {file_name}", file=file_obj)
    file_obj.close()


if __name__ == "__main__":
    base_name = __file__[:-3]
    file_name = base_name + ".data.txt"
    main(file_name)
