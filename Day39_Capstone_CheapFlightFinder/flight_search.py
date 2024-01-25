import secrets
import requests
from datetime import datetime, timedelta

TEQUILA_ENDPOINT = secrets.TEQUILA_ENDPOINT
TEQUILA_API_KEY = secrets.TEQUILA_API_KEY


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def search_city_iata_code(self, details):
        location_url = f"{TEQUILA_ENDPOINT}/locations/query"

        body = {"term": details["city"], "location_types": "city", "limit": 1}

        response = requests.get(
            url=location_url, params=body, headers={"apikey": TEQUILA_API_KEY}
        )
        response.raise_for_status()

        locations = response.json()["locations"]
        return locations[0]["code"]

    def search_for_deals(self, destination):
        search_url = f"{TEQUILA_ENDPOINT}/search"

        tomorrow = datetime.today() + timedelta(days=1)

        params = {
            "fly_from": "city:AMS",
            "fly_to": f"city:{destination['iataCode']}",
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": (tomorrow + timedelta(days=6 * 30)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "price_to": destination["lowestPrice"],
            "curr": "EUR",
        }

        response = requests.get(
            url=search_url, params=params, headers={"apikey": TEQUILA_API_KEY}
        )
        response.raise_for_status()
        data = response.json()

        return data
