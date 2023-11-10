import datetime
import os
import requests


print(os.environ['NUTRI_API_KEY'])

nutri_api_id = os.environ['NUTRI_API_ID']
nutri_api_key = os.environ['NUTRI_API_KEY']

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_header = {
    "x-app-id": nutri_api_id,
    "x-app-key": nutri_api_key,
    "Content-Type": "application/json"
}

nutri_params = {
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 177,
    "age": 27
}

sheety_endpoint = "https://api.sheety.co/5d834a1f9d7c249a6f8ec4d4d7f7a215/workoutTrackerUdemy/exercises"

sheety_header = {
    "Authorization": os.environ['SHEETY_BEARER_TOKEN']
}


# What to input
nutri_params['query'] = input("list your activities and their durations : ")

# capture response
response = requests.post(url=nutri_endpoint, json=nutri_params, headers=nutri_header)
data = response.json()

# loop through exercises
exercises = data['exercises']

for e in exercises:
    body = {
        "exercise": {
            "date": datetime.datetime.today().strftime("%Y-%m-%d"),
            "time": datetime.datetime.today().strftime("%H:%M:%S"),
            "exercise": e["name"].title(),
            "duration": e["duration_min"],
            "calories": e["nf_calories"]
        }
    }

    sheets_response = requests.post(sheety_endpoint, json=body, headers=sheety_header)
    print(sheets_response.text)

