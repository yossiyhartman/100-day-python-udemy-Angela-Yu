import datetime
import datetime as dt
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def ask_user_for_date():
    doi = ''

    try:
        doi = input('What year would you like to travel to? Type in a date (FORMAT YYYY-MM-DD): ')
        doi = dt.datetime.strptime(doi, "%Y-%m-%d")
    except ValueError:
        print('You did not enter a valid date.')

    return doi


def get_website(doi):
    base_url = "https://www.billboard.com/charts/hot-100/"
    response = requests.get(url=f"{base_url}{doi.date()}")
    response.raise_for_status()

    return response.text


def scrape_website_for_songs(website: str):
    soup = BeautifulSoup(website, "html.parser")
    songs_tag = soup.select('.chart-results-list ul li ul li h3')
    songs = [tag.getText().strip() for tag in songs_tag]

    return songs


def auth_spotify():
    SPOTIFY_ID = ""
    SPOTIFY_SECRET = ""

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://localhost",
            client_id=SPOTIFY_ID,
            client_secret=SPOTIFY_SECRET,
            show_dialog=True,
            cache_path="token.txt",
            username="Yossi Hartman",
        )
    )

    return sp


def get_song_uris(sp, year, songs: list):
    URIs = []

    for song in songs:
        results = sp.search(q=f"track:{song} year:{year}", type='track', limit=1)

        try:
            URIs.append(results['tracks']['items'][0]['uri'])
        except IndexError:
            continue

    return URIs


def add_to_playlist(sp, year, songs_uris):
    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(user_id, f'Billboard top {year}', public=False, description='')

    sp.playlist_add_items(playlist['id'], songs_uris)


if __name__ == '__main__':
    doi = ask_user_for_date()
    website = get_website(doi)
    songs = scrape_website_for_songs(website)
    sp = auth_spotify()
    uris = get_song_uris(sp, doi.year, songs)
    add_to_playlist(sp, doi.year, uris)
