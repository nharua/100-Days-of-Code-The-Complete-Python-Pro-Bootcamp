programmingDictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
# Bug, Function: Key
# "An error in a program that prevents the program from running as expected.": Value of dictionary

# Retrieving a key of dictionary
print(programmingDictionary["Bug"])

# Adding new item to dictionary
programmingDictionary["Loop"] = "The action of doing something over and over again"
print(programmingDictionary)

# Create a empty dictionary
emptyDictionary = {}

# Wipe an existing dictionary
programmingDictionary = {}
print(programmingDictionary)

# Editing a item in dictionary
programmingDictionary["Bug"] = "A moth in your computer"
print(programmingDictionary["Bug"])

# Loop through a dictionary

programmingDictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}
print(f"all programmingDictionary dictionary {programmingDictionary}")
for key in programmingDictionary:
    print(key)
    print(programmingDictionary[key])
