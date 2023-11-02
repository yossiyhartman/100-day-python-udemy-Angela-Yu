import time

import requests
import datetime as dt

API_URL_SR_SS = 'https://api.sunrise-sunset.org/json'
API_URL_ISS = 'http://api.open-notify.org/iss-now.json'

RADIUS = 5

COORDINATES = {
    'latitude': 52.238221,
    'longitude': 4.786736,
}

PARAMETERS = {
    'latitude': COORDINATES['latitude'],
    'longitude': COORDINATES['longitude'],
    'formatted': 0
}

def get_SR_SS_data():
    response = requests.get(API_URL_SR_SS, PARAMETERS)
    response.raise_for_status()

    data = response.json()

    return {key: data['results'][key] for key in ['sunrise', 'sunset']}


def get_ISS_position():
    response = requests.get(API_URL_ISS)
    response.raise_for_status()

    return response.json()['iss_position']

def within_radius(cor):
    return ((COORDINATES['latitude'] - cor['latitude'])**2 + (COORDINATES['longitude'] - cor['longitude'])**2)**(1/2) < RADIUS

def is_nighttime(day_info):
    return (day_info['date'].hour < day_info['sunrise_hour']) or ( day_info['sunset_hour'] < day_info['date'].hour)


today = {
    'date': dt.datetime.today(),
    'sunrise_hour': 0,
    'sunset_hour': 0
}

sunrise_sunset_data = get_SR_SS_data()
today['sunrise_hour'] = dt.datetime.strptime(sunrise_sunset_data['sunrise'], '%Y-%m-%dT%H:%M:%S+00:00').hour
today['sunset_hour'] = dt.datetime.strptime(sunrise_sunset_data['sunset'], '%Y-%m-%dT%H:%M:%S+00:00').hour

ISS_position = get_ISS_position()
ISS_position = {key: float(ISS_position[key]) for key in ISS_position}

if within_radius(ISS_position) and is_nighttime(today):
    print('do something')