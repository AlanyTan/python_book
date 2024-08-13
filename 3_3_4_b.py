MIN_VOWLS = 3
phrase = input(f"# Enter text to check if it has more than {MIN_VOWLS} vowls:")
vowls = 0
for letter in phrase:
    if letter in 'aeiouAEIOU':
        vowls += 1

    if vowls >= MIN_VOWLS:
        print(f"# {phrase} as more than {MIN_VOWLS} vowls")
        break
else:
    print(f"# {phrase} only as {vowls} vowls.")

########### 1st run #############
# Enter text to check if it has more than 3 vowls:contratulations
# contratulations as more than 3 vowls


########### 2nd run ##############
# Enter text to check if it has more than 3 vowls:Hello
# Hello only as 2 vowls.
