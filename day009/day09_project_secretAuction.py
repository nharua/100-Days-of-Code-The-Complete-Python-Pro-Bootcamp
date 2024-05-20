from replit import clear

# HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction program.")
end_game = False
data = {}
while not end_game:
    name = input("What is your name? ")
    bid = int(input("What's your bid? "))
    data[name] = bid
    answer = input("Are there any other bidder? Type 'yes' or 'no' ")
    if answer == "no":
        end_game = True
    else:
        clear()
max_bid = 0
for key in data:
    if data[key] > max_bid:
        max_bid = data[key]
        winner = key

print(f"The winner is {winner} with the bid of ${max_bid}")
