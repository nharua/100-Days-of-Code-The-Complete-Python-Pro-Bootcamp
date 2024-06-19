# The two primary data structures of pandas
# 1. Series (1-dimensional): this is a column of csv file
# 2. DataFrame (2-dimensional): All table of csv file

import pandas

data = pandas.read_csv("day025/weather_data.csv")

data_dict = data.to_dict()

print(data_dict)

temp_list = data["temp"].to_list()

print(temp_list)

average = sum(temp_list) / len(temp_list)

print(average)

# the another way to calculate the average

average = data["temp"].mean()
print(average)

# maximum data in Series

max = data["temp"].max()

print(max)

# get data in Columns
print(data["condition"])
print(data.condition)  # the same way to get data in a column

# get data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.temp[0])
print(type(monday.temp))

# Create dataframe from scratch
data_dict = {"student": ["Amy", "James", "Angela"], "score": [76, 56, 65]}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("day025/new_data.csv")
