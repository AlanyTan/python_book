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
        data = file.read()
        texts = data.split("\n")
    except FileNotFoundError:
        print(f"#  in exept block, the file {fname} was not found.")
    except Exception as e:
        print(f"  An unexpected error occurred: {e}")
    else:
        print(f"#  in else block finished reading file properly.")
        return texts[0]
    finally:
        if file:
            file.close()
        print(f"#  in finally block: File closed.")
    
    print(f"#  func safe_read_file ended with errors.")

def main(fnames: list[str]) -> None:
    for fname in fnames:
        print(f"# Trying {fname}...")
        print(f"# 1st line of text in file:{safe_read_file(fname)}")

if __name__ == "__main__":
    fnames = [__file__, "donot.exist"]
    main(fnames)
    
# Trying /home/alan/Documents/Python.book/m8_1_4.py...
#  in else block finished reading file properly.
#  in finally block: File closed.
# 1st line of text in file:"""Demo try-except-else-finally structure"""
# Trying donot.exist...
#  in exept block, the file example.txt was not found.
#  in finally block: File closed.
#  func safe_read_file ended with errors.
# 1st line of text in file:None
