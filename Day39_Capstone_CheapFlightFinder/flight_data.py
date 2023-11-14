import datetime as dt

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.deals = {}

    def extract_deal(self, deal):\

        to = deal["route"][0]["cityTo"]

        if self.deals.get(to) is None:
            self.deals[to] = []

        details = {
            "price": deal['price'],
            "origin_city": deal["route"][0]["cityFrom"],
            "origin_airpoirt": deal["route"][0]["flyFrom"],
            "destination_city": deal["route"][0]["cityTo"],
            "destination_airpoirt": deal["route"][0]["flyTo"],
            "departure_date": dt.datetime.fromtimestamp(deal['route'][0]['dTime']).strftime("%d-%m-%Y"),
            "return_date": dt.datetime.fromtimestamp(deal['route'][1]['dTime']).strftime("%d-%m-%Y"),
            "days": deal['nightsInDest'],
        }

        self.deals[to].append(details)

