def safe_read_file(fname: str) -> str:
    try:
        file = None
        file = open(fname, "r")
        data = file.read()
        texts = data.split("\n")
        return texts[0]
    except FileNotFoundError:
        print(f"# The file {fname} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if file:
            file.close()
        print(f"# finally block: File closed.")

def main(fnames: list[str]) -> None:
    for fname in fnames:
        print(f"#Trying {fname}...")
        print(f"#1st line of text in file:{safe_read_file(fname)}")

if __name__ == "__main__":
    fnames = [__file__, "example.txt"]
    main(fnames)
    
#Trying C:/Users/me/MyDocuments/python_book/8_1_4.py...
# finally block: File closed.
#1st line of text in file:def safe_read_file(fname: str) -> str:
#Trying example.txt...
# The file example.txt was not found.
# finally block: File closed.
#1st line of text in file:None

