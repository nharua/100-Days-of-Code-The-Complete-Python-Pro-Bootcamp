"""
Instructions
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1

Example Input
L
Y
N
Example Output
Thank you for choosing Python Pizza Deliveries!
Your final bill is: $28.
"""

print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? S, M, or L
add_pepperoni = input()  # Do you want pepperoni? Y or N
extra_cheese = input()  # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
cost = 0
if size == "S":
    cost = 15
    if add_pepperoni == "Y":
        cost = cost + 2
    if extra_cheese == "Y":
        cost = cost + 1
if size == "M":
    cost = 20
    if add_pepperoni == "Y":
        cost = cost + 3
    if extra_cheese == "Y":
        cost = cost + 1
if size == "L":
    cost = 25
    if add_pepperoni == "Y":
        cost = cost + 3
    if extra_cheese == "Y":
        cost = cost + 1

print(f"Your final bill is: ${cost}.")
