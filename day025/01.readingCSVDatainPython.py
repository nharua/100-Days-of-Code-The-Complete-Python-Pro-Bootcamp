import csv
import pandas

with open("day025/weather_data.csv", "r") as file:
    print(file.readlines())


with open("day025/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))

print(temperature)


data = pandas.read_csv("day025/weather_data.csv")
print(data)
print(data["temp"])
