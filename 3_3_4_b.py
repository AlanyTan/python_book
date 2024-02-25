secret_word = 'Hello'
GUESSED_TO_WIN = 2
guessed = 0
for letter in secret_word:
    guess = input("#==Guess this letter:")
    if guess == letter:
        print(f"#  yeah!")
        guessed += 1
    else:
        print(f"#  nope")
    if guessed >= GUESSED_TO_WIN:
        print(f"# Congraulations! you guessed {guessed} letters correctly.")
        break
else:
    print(f"#Sorry, you've only guessed {guessed} letters correctly.")
    

########### 1st run #############
#==Guess this letter:H
#  yeah!
#==Guess this letter:a
#  nope
#==Guess this letter:p
#  nope
#==Guess this letter:p
#  nope
#==Guess this letter:y
#  nope
#Sorry, you've only guessed 1 letters correctly.

########### 2nd run ##############
#==Guess this letter:H
#  yeah!
#==Guess this letter:e
#  yeah!
# Congraulations! you guessed 2 letters correctly.
