import random

# Get your own ASCII text
#  https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%200
from art import logo

numberGuess = random.randint(1, 100)
# print(numberGuess)
# Welcom to game
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5


while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > numberGuess:
        attempts -= 1
        print("Too high.")
    elif guess < numberGuess:
        attempts -= 1
        print("Too low.")
    if guess == numberGuess:
        print(f"You got it! The answer is {numberGuess}")
        break
if attempts == 0:
    print("You lose")
