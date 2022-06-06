def convert_temp(temp_c):
    temp_f = 1.8*temp_c + 32
    return temp_f

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

weather_f = {day:convert_temp(temp_c) for (day, temp_c) in weather_c.items()}

print(weather_f)