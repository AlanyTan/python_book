def main(file_name: str) -> None:
    file_obj = open(file_name, 'w+', encoding='utf-8')
    print("Writing", "numbers like", 2, "booleans like", True, file=file_obj)
    print(f"The filename of which I am writing into is {file_name}", file=file_obj)
    file_obj.close()


if __name__ == "__main__":
    file_name = __file__ + ".data.txt"
    main(file_name)
