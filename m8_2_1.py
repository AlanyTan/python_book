"""Demo with structure inside try-except."""
def safe_read_file(fname: str) -> str:
    """open the given filename, read it's first line and return it.
    
    It tries to open the given filename, and read the first line
    if run into exceptions, will report the error, otherwise report 
    the read is finished. With will not try to close the file if open
    failed, so there will not be print message asking user if the file
    has ever been opened.

    Args:
        fname: string representing the file name to open.

    Returns:
        the first line of the file as string.
    """
    try:
        with open(fname, "r") as file:
            data = file.readline()
            texts = data.strip()
        return texts
    except FileNotFoundError:
        print(f"# The file {fname} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main(fnames: list[str]) -> None:
    """main func demo sending different denominators to save_divide.
    
    Args:
        list_of_numbers_to_try: a list containing numbers to be used
        as denominator when trying to call save_divide.
    """
    for fname in fnames:
        print(f"#Trying {fname}...")
        print(f"#1st line of text in file:{safe_read_file(fname)}")

if __name__ == "__main__":
    file_names = [__file__, "example.txt"]
    main(file_names)
    
#Trying C:\Users\alan\OneDrive\Documents\python_book\8_1_4.py...
#1st line of text in file:def safe_read_file(fname: str) -> str:
#Trying example.txt...
# The file example.txt was not found.
#1st line of text in file:None
