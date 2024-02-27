SKIP_WORD = 'skip'
def main(file_name: str) -> None:
    # first create the file with content
    file_w = open(file_name, 'w+', encoding='utf-8')
    file_content = [
        "abc.dev\n",
        "skip\n",
        "123\n"
    ]
    file_w.writelines(file_content)
    file_w.close()

    #next read from the file in place of user input
    file_r = open(file_name, 'r', encoding='utf-8')
    count = 0
    while content := file_r.readline().strip("\n"):
        if content := '' if content == SKIP_WORD else content:
            print(f"# You entered: {content}")
            count += 1
            
        for letter in content:
            match letter:
                case '.':
                    print(f"#..Reached period, abort rest.")
                    break
                case '!':
                    print(f"#!!Reached exclaimation mark, aboar the whole thing!")          
                    break
                case _:
                    print(f"#   {letter}'s ASCII code is {ord(letter)}")
        
    print(f"## You entered {count} strings in total")
    file_r.close()

if __name__ == "__main__":
    base_name = __file__[:-3]
    file_name = base_name + ".data.txt"
    main(file_name)

# You entered: abc.dev
#   a's ASCII code is 97
#   b's ASCII code is 98
#   c's ASCII code is 99
#..Reached period, abort rest.
# You entered: 123
#   1's ASCII code is 49
#   2's ASCII code is 50
#   3's ASCII code is 51
## You entered 2 strings in total
