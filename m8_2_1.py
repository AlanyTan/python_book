def safe_read_file(fname: str) -> str:
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
    for fname in fnames:
        print(f"#Trying {fname}...")
        print(f"#1st line of text in file:{safe_read_file(fname)}")

if __name__ == "__main__":
    fnames = [__file__, "example.txt"]
    main(fnames)
    
#Trying C:\Users\alan\OneDrive\Documents\python_book\8_1_4.py...
#1st line of text in file:def safe_read_file(fname: str) -> str:
#Trying example.txt...
# The file example.txt was not found.
#1st line of text in file:None
