# Function with outputs
def format_string(text):
    result = text.title()
    return result


name = input("Give me your fullname: ")
name = format_string(name)
print(name)
