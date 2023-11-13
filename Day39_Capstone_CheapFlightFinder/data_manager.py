import requests

sheety_endpoint = "https://api.sheety.co/5d834a1f9d7c249a6f8ec4d4d7f7a215/udemyFlightDeals/prices"
sheety_token = "Bearer IUHANGVLJSNHVURIKFADHFJILUSHNRIOLK"
auth_header = {
    "Authorization": f"{sheety_token}"

}
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        pass

    def retrieve(self) -> dict:
        """
            Retrieves the data from the Google Spreadsheet

            :return: the data
        """

        response = requests.get(url=sheety_endpoint, headers=auth_header)
        response.raise_for_status()

        return response.json()

    def update_deal(self, deal):
        put_url = f"{sheety_endpoint}/{deal['id']}"

        body = {
            "price": deal
        }

        response = requests.put(url=put_url, json=body, headers=auth_header)
        print(response)



