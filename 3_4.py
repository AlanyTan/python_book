SKIP_WORD = 'skip'
count_regular = count_total = 0
while (user_input := input("# ==Enter 'exit' to stop:")) != 'exit':
    if content := '' if user_input == SKIP_WORD else user_input:
        print(f"# You entered: {content}")
        count_total += 1

    for letter in content:
        match letter:
            case '.' as period:
                print(f"# Reached '{period}', skip rest.")
                break
            case '!' as exclaimation:
                print(f"# Reached '{exclaimation}', abort the whole thing!")
                content = 'exit'
                break
            case _:
                print(f"#   {letter}'s ASCII code is {ord(letter)}")
    else:
        count_regular += bool(content)

    if content == 'exit':
        break

else:
    print(f"## You entered {count_total} in total,\
          of which {count_regular} has no terminators.")

# ==Enter 'exit' to stop:abc.def
# You entered: abc.def
#   a's ASCII code is 97
#   b's ASCII code is 98
#   c's ASCII code is 99
# Reached '.', skip rest.
# ==Enter 'exit' to stop:skip
# ==Enter 'exit' to stop:def
# You entered: def
#   d's ASCII code is 100
#   e's ASCII code is 101
#   f's ASCII code is 102
# ==Enter 'exit' to stop:exit
# You entered 2 in total,          of which 1 has no terminators.

# ==Enter 'exit' to stop:ghi!jkl
# You entered: ghi
#   g's ASCII code is 103
#   h's ASCII code is 104
#   i's ASCII code is 105
# Reached '!', aboar the whole thing!
