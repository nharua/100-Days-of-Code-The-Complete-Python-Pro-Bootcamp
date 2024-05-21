import re
from art import logo


# Define function
# Add
def add(a, b):
    return a + b


# Subtract
def sub(a, b):
    return a - b


# Multiply
def mult(a, b):
    return a * b


# Divide
def div(a, b):
    return a / b


calc = {"+": add, "-": sub, "*": mult, "/": div}
print(logo)
num1 = int(input("What's the 1st number? "))
for key in calc:
    print(key)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the 2nd number? "))

result = calc[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {result}")
be_continue = True
while be_continue:
    choice = input(
        f"Type 'y' to continue to calculate with {result}, or type 'n' to exist: "
    )
    if choice == "n":
        be_continue = False
    elif choice == "y":
        operation_symbol = input("Pick an operation: ")
        num3 = int(input("What's the next number? "))
        last_number = result
        result = calc[operation_symbol](result, num3)
        print(f"{last_number} {operation_symbol} {num3} = {result}")
