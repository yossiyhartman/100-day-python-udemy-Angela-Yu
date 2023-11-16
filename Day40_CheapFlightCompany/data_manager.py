from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/5d834a1f9d7c249a6f8ec4d4d7f7a215/udemyFlightDeals/prices"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    @staticmethod
    def add_user(firstname, lastname, email):
        body = {
            "user": {
                'firstName': firstname,
                'lastName': lastname,
                'email': email
            }
        }

        response = requests.post(
            url=f"{SHEETY_USERS_ENDPOINT}",
            json=body
        )

        print(response.text)
