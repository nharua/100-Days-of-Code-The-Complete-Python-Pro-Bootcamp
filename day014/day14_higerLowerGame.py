from art import logo, vs
from game_data import data
import random
from replit import clear


def follower(name):
    global data
    for item in data:
        if item["name"] == name:
            return item["follower_count"]


def compare(a, b):
    if a > b:
        return True
    else:
        return False


correct = True
final_score = 0
clear()
print(logo)
while correct:
    a_item = random.choice(data)
    b_item = random.choice(data)
    print(
        f"Compare A: {a_item['name']}, a {a_item['description']}, from {a_item['country']}"
    )
    print(vs)
    print(
        f"Compare B: {b_item['name']}, a {b_item['description']}, from {b_item['country']}"
    )
    answer = input("Who has more followers? Type 'A' or 'B' ").lower()
    if answer == "a" and compare(a_item["follower_count"], b_item["follower_count"]):
        final_score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {final_score}.")
    elif answer == "b" and compare(b_item["follower_count"], a_item["follower_count"]):
        final_score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {final_score}.")
    else:
        correct = False
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {final_score}")
