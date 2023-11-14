# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()

# sheet_data = data_manager.retrieve_data_from_sheet()
# TODO: uncomment this in the final version
sheet_data = data_manager.data = [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 100},
                                  {'city': 'Berlin', 'iataCode': 'BER', 'id': 3, 'lowestPrice': 100},
                                  {'city': 'Athens', 'iataCode': 'ATH', 'id': 4, 'lowestPrice': 400},
                                  # {'city': 'Sydney', 'iataCode': 'SYD', 'id': 5, 'lowestPrice': 1000},
                                  # {'city': 'Istanbul', 'iataCode': 'IST', 'id': 6, 'lowestPrice': 95},
                                  # {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'id': 7, 'lowestPrice': 414},
                                  # {'city': 'New York', 'iataCode': 'NYC', 'id': 8, 'lowestPrice': 240},
                                  # {'city': 'San Francisco', 'iataCode': 'SFO', 'id': 9, 'lowestPrice': 260},
                                  # {'city': 'Cape Town', 'iataCode': 'CPT', 'id': 10, 'lowestPrice': 378}
                                  ]


# if the Iata Codes are not filled in yet, fill in the codes
if sheet_data[0]['iataCode'] == "":

    for destination in sheet_data:
        destination['iataCode'] = flight_search.search_city_iata_code(destination)

    data_manager.update_iata_codes()

# Search for deals
for i, destination in enumerate(sheet_data):

    deals = flight_search.search_for_deals(destination)

    for deal in deals['data']:
        flight_data.extract_deal(deal)

pprint(flight_data.deals)