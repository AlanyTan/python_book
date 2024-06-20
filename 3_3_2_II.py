count = 0
while (user_input := input("#==Enter 'exit' to stop: ")) != 'exit':
    print(f"# You entered: {user_input}")
    count += 1
    for letter in user_input:
        print(f"#   {letter}'s ASCII code is {ord(letter)}")
print(f"## You entered {count} strings in total")

#==Enter 'exit' to stop: abc
# You entered: abc
#   a's ASCII code is 97
#   b's ASCII code is 98
#   c's ASCII code is 99
#==Enter 'exit' to stop:  
# You entered:  
#    's ASCII code is 32
#==Enter 'exit' to stop: 
# You entered: 
#==Enter 'exit' to stop: exit
## You entered 3 strings in total
