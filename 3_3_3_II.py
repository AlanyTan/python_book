count = 0
not_broken = True
while not_broken and (user_input := input("#==Enter 'exit' to stop): ")) != 'exit':
    if not user_input or user_input == 'skip' :
        continue
    print(f"# You entered: {user_input}")
    
    for letter in user_input:
        if letter == '.':
            print(f"#..Reached period, abort rest.")
            break
        
        if letter == '!':
            print(f"#!!Reached exclaimation mark, aboar the whole thing!")
            not_broken = False            
            break
        
        print(f"#   {letter}'s ASCII code is {ord(letter)}")
        
    count += 1
    
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
