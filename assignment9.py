
import random

# Step 1: Generate a random number
target = random.randint(1, 10)

# Step 2: Ask the user to guess
while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == target:
            print("You guessed it!")
            break
        elif guess < target:
            print("Too low!")
        else:
            print("Too high!")
    except ValueError:
        print("Please enter a valid number.")
