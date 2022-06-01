import pandas as pd

data = pd.read_csv('weather_data.csv')
# print(type(data))
# print(type(data['temp']))

# # Dataframe
# data_dict = data.to_dict()
# print(data_dict)

# # Series
# temp_list = data['temp'].to_list()
# print(temp_list)

# print(f"Average: {data['temp'].mean()}")
# print(f"Maximum: {data['temp'].max()}")

# # Get data in columns
# print(data.condition)

# Get data in rows
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# monday_temp = int(monday.temp)
# monday_temp_f = 1.8 * monday_temp + 32
# print(monday_temp_f)

# Create dataframe from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv('new_data.csv')