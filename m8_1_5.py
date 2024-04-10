"""Demo nested try-except structure"""
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
        try:
            file = open(fname, "r")
            data = file.read()
            texts = data.split("\n")
        except FileNotFoundError:
            print(f"#   in exept block, the file {fname} was not found.")
        except Exception as e:
            print(f"   An unexpected error occurred: {e}")
        else:
            print(f"#   in else block finished reading file properly.")
            return texts[0]
        finally:
            file.close()
            print(f"#   in finally block: File closed.")
        
    except:
        print(f"#  file can't be closed, maybe it was never opened?")

def main(fnames: list[str]) -> None:
    for fname in fnames:
        print(f"# Trying {fname}...")
        print(f"# 1st line of text in file:{safe_read_file(fname)}")

if __name__ == "__main__":
    fnames = [__file__, "example.txt"]
    main(fnames)
    
# Trying /home/alan/Documents/Python.book/m8_1_5.py...
#   in else block finished reading file properly.
#   in finally block: File closed.
# 1st line of text in file:"""Demo nested try-except structure"""
# Trying example.txt...
#   in exept block, the file example.txt was not found.
#  file can't be closed, maybe it was never opened?
# 1st line of text in file:None
