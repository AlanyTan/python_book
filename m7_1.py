def main(file_name: str) -> None:
    """Main func demo file creation, open for read and close.

    Will first open file_name for write, create if not yet exist, 
    truncate the file if already exist. Then close it.
    Next, open file_name for read, then close it.
    
    
    Args:
        file_name: string representing file name to create and open.

    Returns: 
        None
    """
    file_w = open(file_name,'w', encoding='utf-8')
    print(f"# {type(file_w)=}, {file_w.closed=}")
    file_w.close()
    print(f"# {type(file_w)=}, {file_w.closed=}")
    
    file_rb = open(file_name, 'r+b')
    print(f"# {type(file_rb)=}, {file_rb.closed=}")
    file_rb.close()
    print(f"# {type(file_rb)=}, {file_rb.closed=}")

if __name__ == "__main__":
    base_name = __file__[:-3]
    file_name = base_name + ".data"
    main(file_name)

# type(file_w)=<class '_io.TextIOWrapper'>, file_w.closed=False
# type(file_w)=<class '_io.TextIOWrapper'>, file_w.closed=True
# type(file_rb)=<class '_io.BufferedRandom'>, file_rb.closed=False
# type(file_rb)=<class '_io.BufferedRandom'>, file_rb.closed=True
