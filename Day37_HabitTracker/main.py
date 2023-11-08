import datetime

import requests

PIXELA_URL = "https://pixe.la/v1/users"
USERNAME = "yossiyanou"
TOKEN = "ditiseenkeyvoorpixelaapi"

USER_PARAMS = {
    "token": TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create a user
# response = requests.post(url=PIXELA_URL, json=USER_PARAMS)
# print(response.text)

# Create a graph
graph_params = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": 'h',
    "type": "float",
    "color": "shibafu"
}

# response = requests.post(url=f"{PIXELA_URL}/{USERNAME}/graphs", json=graph_params, headers=headers)
# print(response.text)

# Post a pixel
pixel_params = {
    "date": datetime.datetime.today().strftime("%Y%m%d"),
    'quantity': "5"
}

# response = requests.post(url=f"{PIXELA_URL}/{USERNAME}/graphs/{graph_params['id']}", json=pixel_params, headers=headers)
# print(response.text)

# update a pixel
update_date = datetime.datetime.today().strftime("%Y%m%d")

update_pixel_params = {
    "quantity": "10"
}
response = requests.put(url=f"{PIXELA_URL}/{USERNAME}/graphs/{graph_params['id']}/{update_date}", json=update_pixel_params, headers=headers)
print(response.text)