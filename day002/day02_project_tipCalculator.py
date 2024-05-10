print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
tip_pay = (bill * tip) / 100
people = int(input("How many people to split the bill? "))
pay = round((bill + tip_pay) / people, 2)
print(f"Each person should pay: ${pay}")
