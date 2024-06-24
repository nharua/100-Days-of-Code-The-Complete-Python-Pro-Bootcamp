# NOTE:
# new_dict ={new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.item()}
# new_dict = {new_key:new_value for (key, value) in dict.item() if test}
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {name: random.randint(1, 100) for name in names}
print(students_scores)

passed_students = {
    student: score for (student, score) in students_scores.items() if score > 50
}
print(passed_students)
