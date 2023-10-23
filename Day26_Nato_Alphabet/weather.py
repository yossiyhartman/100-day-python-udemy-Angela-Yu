days_temperature_c ={
    "Monday": 21,
    "Tuesday": 17,
    "Wednesday": 25,
    "Thursday": 24,
    "Friday": 30,
    "Saturday": 27,
    "Sunday": 20,
}

days_temperature_f = {day: (c * 9 / 5) + 32 for day, c in days_temperature_c.items()}

print(days_temperature_f)