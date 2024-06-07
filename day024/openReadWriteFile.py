file = open("day024/my_file.txt")
content = file.read()

print(content)
file.close()

# the another way to open and read the file
with open("./day024/my_file.txt") as file:
    content = file.read()
    print(content)

# write content into my_file.txt
with open("./day024/my_file.txt", mode="w") as file:
    file.write("I'm 47 years old\n")

# write more content into my_file.txt - append mode
with open("./day024/my_file.txt", mode="a") as file:
    file.write("I'm an engineer as Network Administrator\n")

with open("./day024/my_file.txt", mode="r") as file:
    print(file.read())
