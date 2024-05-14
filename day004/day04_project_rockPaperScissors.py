rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
import random

rockPaperScissors = [rock, paper, scissors]
yourChoice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
computerChoice = random.randint(0, 2)
if yourChoice == computerChoice:
    print(rockPaperScissors[yourChoice])
    print("Computer Chose: \n", rockPaperScissors[computerChoice])
    print("Deal")
elif yourChoice == 0 and computerChoice == 1:
    print(rockPaperScissors[yourChoice])
    print("Computer Chose: \n", rockPaperScissors[computerChoice])
    print("You lose")
elif yourChoice == 1 and computerChoice == 2:
    print(rockPaperScissors[yourChoice])
    print("Computer Chose: \n", rockPaperScissors[computerChoice])
    print("You lose")
elif yourChoice == 3 and computerChoice == 0:
    print(rockPaperScissors[yourChoice])
    print("Computer Chose: \n", rockPaperScissors[computerChoice])
    print("You lose")
else:
    print(rockPaperScissors[yourChoice])
    print("Computer Chose: \n", rockPaperScissors[computerChoice])
    print("You win")
