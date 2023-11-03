import requests

API_URL = 'https://opentdb.com/api.php?amount=20&difficulty=easy&type=boolean'

response = requests.get(API_URL)
response.raise_for_status()

question_data = response.json()['results']
