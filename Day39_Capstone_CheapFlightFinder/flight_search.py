import pprint

import requests

flight_url = "https://api.tequila.kiwi.com"
flight_api_key = "q3_zrc65tI5qsWBczJMU99HIAlg3ApSY"

header = {
    "apikey": flight_api_key
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def search_city_iata_code(self, details):

        body = {
            "term": details["city"],
            'location_types': "city",
            "limit": 1
        }

        response = requests.get(url=f"{flight_url}/locations/query", params=body, headers=header)
        response.raise_for_status()

        locations = response.json()["locations"]
        code = locations[0]['code']

        details['iataCode'] = code
