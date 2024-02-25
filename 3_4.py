SKIP_WORD = 'skip'
count = 0
content = ''
while content != 'exit':
    if content := '' if content == SKIP_WORD else content:
        print(f"# You entered: {content}")
        count += 1
        
    for letter in content:
        match letter:
            case '.':
                print(f"#..Reached period, abort rest.")
                content = ''
                break
            case '!':
                print(f"#!!Reached exclaimation mark, aboar the whole thing!")          
                content = 'exit'
                break
            case _:
                print(f"#   {letter}'s ASCII code is {ord(letter)}")
    else:
        content = input("#==Enter 'exit' to stop:")
    
print(f"## You entered {count} strings in total")

#==Enter 'exit' to stop): abc.def
# You entered: abc.def
#   a's ASCII code is 97
#   b's ASCII code is 98
#   c's ASCII code is 99
#..Reached period, abort rest.
#==Enter 'exit' to stop): abc!def
# You entered: abc!def
#   a's ASCII code is 97
#   b's ASCII code is 98
#   c's ASCII code is 99
#!!Reached exclaimation mark, aboar the whole thing!
## You entered 2 strings in total
