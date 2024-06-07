# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Read the invited_name and store in list
names = []
with open(
    "./day024/day24_project_mailMerge/Input/Names/invited_names.txt", "r"
) as file:
    for line in file:
        names.append(line.rstrip())

# print(names)

# Read the letter template and replace [name] with the name in our lists

with open(
    "./day024/day24_project_mailMerge/Input/Letters/starting_letter.txt", "r"
) as file:
    letter_template = file.read()

for name in names:
    letter = letter_template.replace("[name]", name)
    with open(
        f"./day024/day24_project_mailMerge/Output/ReadyToSend/{name}_letter", "w"
    ) as file:
        file.write(letter)

