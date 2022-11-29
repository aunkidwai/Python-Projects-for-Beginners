"""
Task: Below are the steps:

    + Build a Number guessing game, in which the user selects a range.
    + Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
    + Some random integer will be selected by the system and the user has to guess that integer
      in the minimum number of guesses.
"""
import math
import random

# User Input and Output
lower = int(input("Enter Lower bound: "))
upper = int(input("Enter Upper bound: "))

number_to_guess = random.randint(lower, upper)
guesses = round(math.log(upper - lower + 1, 2))
print("You've only {0} chances to guess the integer!\n".format(guesses))

count = 0

while count < guesses:
    count += 1

    # User Guess
    guessed_number = int(input("Guess a number: "))

    # Checking the guesses
    if number_to_guess == guessed_number:
        print("Congratulations!! You guessed it with {0} try(s) remaining". format(guesses-count))
        break
    elif number_to_guess > guessed_number:
        print("You can go higher!!")
    elif number_to_guess < guessed_number:
        print("You should go higher!!")

