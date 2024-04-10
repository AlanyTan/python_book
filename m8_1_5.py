"""Demo nested try-except structure"""
def safe_read_file(fname: str) -> str:
    """open the given filename, read it's first line, and return it. 
    
    It tries to open the given filename, and read the first line, 
    if run into exception, will report the error, otherwise, report
    the read is finished properly. 
    If run into exceptions during closing of the file, it reports 
    the closing error, and ask if the file was ever open.
    
    Args:
        fname: string representing the file name to open.
    
    Returns:
        the first line of the file as a stirng.
    """
    try:
        try:
            file = open(fname, "r")
            data = file.read()
            texts = data.split("\n")
        except FileNotFoundError:
            print(f"#   in exept block, the file {fname} was not found.")
        except Exception as e:
            print(f"   An unexpected error occurred: {e}")
        else:
            print("#   in else block finished reading file properly.")
            return texts[0]
        finally:
            file.close()
            print("#   in finally block: File closed.")
        
    except Exception as e:
        print(f"#  closing file run into exception,{e}, maybe it was never opened?")

def main(fnames: list[str]) -> None:
    """main func demo sending different denominators to save_divide.
    
    Args:
        list_of_numbers_to_try: a list containing numbers to be used
        as denominator when trying to call save_divide.
    """

    for fname in fnames:
        print(f"# Trying {fname}...")
        print(f"# 1st line of text in file:{safe_read_file(fname)}")

if __name__ == "__main__":
    file_names = [__file__, "example.txt"]
    main(file_names)
    
# Trying /home/alan/Documents/Python.book/m8_1_5.py...
#   in else block finished reading file properly.
#   in finally block: File closed.
# 1st line of text in file:"""Demo nested try-except structure"""
# Trying example.txt...
#   in exept block, the file example.txt was not found.
#  file can't be closed, maybe it was never opened?
# 1st line of text in file:None
