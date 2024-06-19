import pandas

data = pandas.read_csv("./day025/2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
gray_count = len(gray_squirrels)
black_count = len(black_squirrels)
red_count = len(red_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count],
}
pandas.DataFrame(data_dict).to_csv("./day025/squirrel_count.csv")
