# Author: Jake Trissel
# Github Username: trisselj
# Date: 07/10/2024
# Description: Reads inputs and compares to initial number printing whther input is > < or = initial number

# Initial prompt for number to guess for
Target = int(input("Enter the integer for the player to guess. "))

#Keeps track of guesses
guess_count = 0
guess = None

# Gameplay loop for guessing
while True:
    guess = int(input("Enter your guess"))
    guess_count += 1
    if guess == Target:
        break
    elif guess > Target:
        print("Too high - try again: ")
    else:
        print("Too low - try again: ")

#Prints out number of guesses
if guess_count == 1:
    print(f"You guessed it in 1 try.")
else:
    print(f"You guessed it in {guess_count} tries!")