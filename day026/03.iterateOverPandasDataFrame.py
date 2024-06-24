import pandas

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# Loop through a dictionary
for key, value in student_dict.items():
    print(key, value)

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

# Loop throughgh a data DataFrame
for key, value in student_dataframe.items():
    print(key, value)

# Loop through rows of a dataframe
for index, row in student_dataframe.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    print(row.score)
