import requests

API_URL = 'https://api.openweathermap.org/data/2.5/weather'

API_KEY: str = 'f45bd754e41d5af330ae63e3a60a15f1'

API_PARAMS = {
    'appid': API_KEY,
    'q': 'Amsterdam',
}

response = requests.get(API_URL, API_PARAMS)
response.raise_for_status()

data = response.json()

weather = data['weather'][0]['id']

print(data, weather)