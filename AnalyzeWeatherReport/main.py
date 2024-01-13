import pandas as pd

# temp = []

# with open('weather_data.csv') as file:
#     weather_list = csv.reader(file)
#     next(weather_list)
#     print(weather_list)
#     for row in weather_list:
#         new_temp = int(row[1])
#         temp.append(new_temp)
#
# print(temp)
# avg=0
# data=pandas.read_csv('weather_data.csv')
# print(data)
# print(data.to_dict()['day'][2])
# for i in data["temp"]:
#     avg += i
#
# print(round(avg/len(data["temp"]),2))
# s = data['temp'].max()
# print(data[data.temp==s])
#
# mon_temp = ((data[data.day == 'Monday'].temp - 32)*5)/9
# print(mon_temp)


data=pd.read_csv('Squirrel_Data.csv')
gb = data.groupby('Primary Fur Color')['Primary Fur Color'].count()
print(gb)
