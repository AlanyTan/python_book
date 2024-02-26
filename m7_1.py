def main() -> None:
    file_w = open("example.tmp",'w', encoding='utf-8')
    print(f"# {type(file_w)=}, {file_w.closed=}")
    file_w.close()
    print(f"# {type(file_w)=}, {file_w.closed=}")
    
    file_rb = open("example.tmp", 'r+b')
    print(f"# {type(file_rb)=}, {file_rb.closed=}")
    file_rb.close()
    print(f"# {type(file_rb)=}, {file_rb.closed=}")

if __name__ == "__main__":
    main()

# type(file_w)=<class '_io.TextIOWrapper'>, file_w.closed=False
# type(file_w)=<class '_io.TextIOWrapper'>, file_w.closed=True
# type(file_rb)=<class '_io.BufferedRandom'>, file_rb.closed=False
# type(file_rb)=<class '_io.BufferedRandom'>, file_rb.closed=True
