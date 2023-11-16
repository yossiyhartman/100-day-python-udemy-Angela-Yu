import requests

SHEETY_USERS_ENDPOINT = "https://api.sheety.co/5d834a1f9d7c249a6f8ec4d4d7f7a215/udemyFlightDeals/users"

def post_new_row(first_name, last_name, email):
    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(url=SHEETY_USERS_ENDPOINT, json=body)
    response.raise_for_status()
    print(response.text)