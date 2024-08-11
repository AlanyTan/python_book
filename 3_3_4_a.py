secret_number = 5
GUESS_LIMIT = 3
attempt = 0

while (attempt := attempt + 1) <= GUESS_LIMIT:
    guess = int(input("#--Guess the number: "))
    if guess == secret_number:
        print("# Congratulations! You guessed it right.")
        break
else:
    print("#Sorry, you've run out of attempts.")

########### 1st run ################
# --Guess the number: 1
# --Guess the number: 2
# --Guess the number: 3
# Sorry, you've run out of attempts.

########### 2nd run ################
# --Guess the number: 3
# --Guess the number: 4
# --Guess the number: 5
# Congratulations! You guessed it right.
