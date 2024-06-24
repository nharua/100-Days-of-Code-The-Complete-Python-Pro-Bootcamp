# TODO:List comprehension
# For LOOP
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 16
    new_list.append(add_1)

# NOTE:rewrite using list comprehension
# new_list = [new_list for item in old_list]
new_list_compreshension = [n + 1 for n in numbers]
print(new_list_compreshension)

new_numbers = [item * 2 for item in range(1, 5)]
print(new_numbers)

# NOTE:Conditional List comprehension
# new_list = [new_item for item in list if test]
name_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

new_name_list = [name for name in name_list if len(name) < 5]
print(new_name_list)

new_name_list_upcase = [name.upper() for name in name_list if len(name) > 4]
print(new_name_list_upcase)
