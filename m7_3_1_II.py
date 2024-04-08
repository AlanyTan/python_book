"""Module demonstrate using .readlines() and list operations to process file content.

This module realize the same functionality as m7_3_1_I, but replace sequential line
processing with .readlines() and list, and generators.

Usage: 
    python -m m7_3_1_II

Note:
    This module will create a test file under the current directory, 
    so please make sure you have write permission in the current dir.
"""
from m7_3_1_I import creat_input_file

SKIP_WORDS = ['skip']

def parse_line(line:str ) -> list:
    """Parse a line based on logic in section 3.4

    For each char in the given line, add its ASCII code to return list.
    Unless it's a '.' or '!' which will abort and ignore everything after it.
    If the line is '\n' or only contain words in the SKIP_WORD list, then 
    the result list will be empty.

    Args:
        line: the str that contains characters to be processed.

    Returns:
        A list of str, each shows the char and its ASCII code.
    """
    result = []
    line = line.strip('\n')
    if line := '' if line in SKIP_WORDS else line:
        result.append(f"# You entered: {line}")
        
    for letter in line:
        match letter:
            case '.':
                result.append(f"#..Reached period, abort rest.")
                break
            case '!':
                result.append(f"#!!Reached exclaimation mark, aboar the whole thing!")          
                break
            case _:
                result.append(f"#   {letter}'s ASCII code is {ord(letter)}")
    return result

def main(file_name: str) -> None:
    """Demo using .readlines() read full content from file.
    
    This function demonstrate using .readlines() to read file lines into
    a list, and use list, map, generator to process the content, but 
    realize the program behavior.
    
    Args:
        file_name: the name of the text file to use.
        
    Returns:
        None
    """
    file_r = open(file_name, 'r', encoding='utf-8')
    contents = file_r.readlines()
    exclaimation_marks = [i for i, s in enumerate(contents) if '!' in s]
    if exclaimation_marks:
        contents[exclaimation_marks[0]+1:]=[]
    result = map(lambda line: map(print, parse_line(line)), contents)

    print(f"## You entered {sum(1 for item in result if list(item))} strings in total")
    file_r.close()

if __name__ == "__main__":
    base_name = __file__[:-3]
    file_name = base_name + ".data.txt"
    if creat_input_file((file_name)):
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
