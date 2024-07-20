"""Module demonstrate using .readline() replacing input().

This module keeps the main program logic as section 3.4 but replaces
input() with .readline() so it takes input from a text file.

Usage: 
    python -m m7_3_2

Note:
    This module will create a test file under the current directory, 
    so please make sure you have write permission in the current dir.
"""

SKIP_WORD = 'skip'
EXAMPLE_CONTENT = ["abc.dev\n",
        "\n",
        "skip\n",
        "123\n",
    ]

def creat_input_file(file_name: str, file_content: list = None) -> bool:
    """Create file with given file_name and write prepared content to it.

    Args: 
        file_name: the name of the file to create and write into.
        file_content: list of str representing the content to be written, optional

    Returns:
        True, if the creation and writing were successful.    
    """
    content = file_content if file_content else EXAMPLE_CONTENT
    file_w = open(file_name, 'w+', encoding='utf-8')
    file_w.writelines(content)
    file_w.close()
    return True

def main(file_name: str) -> None:
    """Demo using .readline() read from file to replace input()
    
    This function demonstrate replacing input() with .readline() but 
    keep all other aspects of the program logic intact.
    
    Args:
        file_name: the name of the text file to use.
        
    Returns:
        None
    """
    file_r = open(file_name, 'r', encoding='utf-8')
    count = 0
    break_again = False
    while line := file_r.readline():
    # the above while can be replaced by a for loop with exact same effect
    # for line in file_r:
        line = line.strip("\n")
        if content := '' if line == SKIP_WORD else line:
            print(f"# Read: {content}")
            count += 1
            
        for letter in content:
            match letter:
                case '.':
                    print("#..Reached period, ignore the rest.")
                    break
                case '!':
                    print("#!!Reached exclaimation mark, abort the whole thing!")          
                    content = SKIP_WORD
                    break
                case _:
                    print(f"#   {letter}'s ASCII code is {ord(letter)}")
        
        if content == SKIP_WORD:
            break

    print(f"## Read {count} strings in total")
    file_r.close()

if __name__ == "__main__":
    base_name = __file__[:-3]
    file_name = base_name + ".data.txt"
    if creat_input_file(file_name):
        main(file_name)

# Read: abc.dev
#   a's ASCII code is 97
#   b's ASCII code is 98
#   c's ASCII code is 99
#..Reached period, abort rest.
# Read: 123
#   1's ASCII code is 49
#   2's ASCII code is 50
#   3's ASCII code is 51
## Read 2 strings in total
