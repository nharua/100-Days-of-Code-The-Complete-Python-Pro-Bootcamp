"""
Instructions
Write a program that calculates and outputs the number of characters in any name. The automated tests will try out lots of different names as the input. Your code should work for any name. Your code should only output the number, no other text is needed.

Hint
Remember, you can use len() around any piece of text to calculate the number of characters.

e.g. https://www.google.com/search?q=how+to+get+the+length+of+a+string+in+python+stack+overflow

Important
Don't add prompt text to the input() function.

e.g. use

✅ name = input()

don't use:

❌ name = input("What's your name?")
"""

num1 = int(input())
num2 = int(input())

print(num1 * num2)

# Option 1 - easy to read
name = input()
lenofname = len(name)
print(lenofname)

# Option 2
print(len(input()))
