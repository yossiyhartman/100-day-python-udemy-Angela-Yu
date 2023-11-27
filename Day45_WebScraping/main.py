from bs4 import BeautifulSoup
import requests

MOVIE_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Retrieve website
response = requests.get(url=MOVIE_URL)
response.raise_for_status()

website = response.text

soup = BeautifulSoup(website, 'html.parser')

titles = soup.select('.gallery .title')

movie_list = []

for title in titles:
    movie_list.insert(0, title.getText() + "\n")

with open('best_movies_of_all_time.txt', mode='w') as file:
    file.writelines(movie_list)
