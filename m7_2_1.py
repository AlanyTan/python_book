def main(file_name: str) -> None:
    file = open(file_name, 'w+', encoding='utf-8')
    print("This is a test", "somemore info", 2, file=file)
    print(f"The filename of which I am writing into is {file_name}", file=file)
    file.close()


if __name__ == "__main__":
    file_name = __file__ + ".data.txt"
    main(file_name)
