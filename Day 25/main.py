#
# with open("weather_data.csv")as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] !="temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
#
#
# # data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# average = sum(temp_list)/len(temp_list)
# highest = max(temp_list)
#
# #Get Data in Columns
# print(data["condition"])
# print(data.condition)
#
# #Get data in row
# print(data[data.day == "Monday"])
#
# #Get data which highest temperature in row
# print(data[data.temp == max(temp_list)])
#
# #Get Monday_data
# Monday = data[data.day == "Monday"]
# #Get Monday_data to fahrenheit
# print(Monday.temp * 9/5 +32)

#Create a dataframe from scratch
# data_dict ={
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,56, 65]
# }
# data = pandas.DataFrame(data_dict )
# print(data)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250827.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"]== "Gray"])
Cinnamon_squirrels_count = len(data[data["Primary Fur Color"]== "Cinnamon"])
Black_squirrels_count = len(data[data["Primary Fur Color"]== "Black"])
White_squirrels_count = len(data[data["Primary Fur Color"]== "White"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black","White"],
    "Count" : [grey_squirrels_count,Cinnamon_squirrels_count ,Black_squirrels_count,White_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count")