from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = '3ed0ef9f3e6c478e9b9f3bc598e01829'
secret = '98860e21363949daab4ba78cdbfd6fb9'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

while True:
    for i in range(0, 999, 50):
        name = "year: 2023"
        result = sp.search(name, type = 'track', limit=50, offset = i)

    x = list(range(0, 50))
    track = []
    track_id = []
    artist = []
    release_date = []
    genre = []
    danceability = []
    energy = []
    loudness = []
    speechiness = []
    popularity = []

    for i in x:
        artists_uri = result['tracks']['items']
        artist.append(artists_uri[i]['artists'][0]['name'])
        track.append(artists_uri[i]['name'])
        track_id.append(artists_uri[i]['id'])
        popularity.append(artists_uri[i]['popularity'])
        q = artists_uri
        release_date.append(q[i]['album']['release_date'])

    audio_details = sp.audio_features(track_id)
    g = range(0,50)
    for i in g:
        energy.append(audio_details[i]['energy'])
        danceability.append(audio_details[i]['danceability'])
        loudness.append(audio_details[i]['loudness'])
        speechiness.append(audio_details[i]['speechiness'])


    spot = pd.DataFrame({"artist":artist , "track": track, "track_id":track_id, "release_date":release_date, "danceability": danceability, "energy":energy, "loudness":loudness, "speechiness":speechiness, "popularity":popularity})

    spot.head()
