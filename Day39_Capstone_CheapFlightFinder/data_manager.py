import requests
import secrets

SHEETY_ENDPOINT = secrets.SHEETY_ENDPOINT
SHEETY_API_KEY = secrets.SHEETY_API_KEY


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.data = {}

    def retrieve_data_from_sheet(self) -> dict:
        response = requests.get(
            url=SHEETY_ENDPOINT, headers={"Authorization": f"{SHEETY_API_KEY}"}
        )
        response.raise_for_status()
        self.data = response.json()["prices"]

        return self.data

    def update_iata_codes(self):
        for destination in self.data:
            put_url = f"{SHEETY_ENDPOINT}/{destination['id']}"

            body = {"price": {"iataCode": destination["iataCode"]}}

            response = requests.put(
                url=put_url, json=body, headers={"Authorization": f"{SHEETY_API_KEY}"}
            )
            print(response.text)
