"""Demo try-except-else-finally structure"""
def safe_read_file(fname: str) -> str:
    """open the given filename, read it's first line, and return it. 
    
    It tries to open the given filename, and read the first line, 
    if run into exception, will report the error, otherwise, report
    the read is finished properly.
    
    Args:
        fname: string representing the file name to open.
    
    Returns:
        the first line of the file as a stirng.
    """
    try:
        file = None
        file = open(fname, "r")
        data = file.readline()
    except FileNotFoundError:
        print(f"#  in exept block, the file {fname} was not found.")
    except Exception as e:
        print(f"  An unexpected error occurred: {e}")
    else:
        print("#  in else block finished reading file properly.")
        return data.strip()
    finally:
        if file:
            file.close()
            print("#  in finally block: File closed.")
        else:
            print("#  in finally block, File was never opened.")

    print("#  func safe_read_file ended with errors.")

def main(fnames: list[str]) -> None:
    """main func demo sending different filename to safe_read_file.
    
    Args:
        fnames: a list containing filename to open and read.
    """
    for fname in fnames:
        print(f"# Trying {fname}...")
        print(f"# 1st line of text in file:{safe_read_file(fname)}")

if __name__ == "__main__":
    file_names = [__file__, "donot.exist"]
    main(file_names)
    
# Trying C:\Users\alan\OneDrive\Documents\python_book\m8_1_4.py...
#  in else block finished reading file properly.
#  in finally block: File closed.
# 1st line of text in file:"""Demo try-except-else-finally structure"""
# Trying donot.exist...
#  in exept block, the file donot.exist was not found.
#  in finally block, File was never opened.
#  func safe_read_file ended with errors.
# 1st line of text in file:None
