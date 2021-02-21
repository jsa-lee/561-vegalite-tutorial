# Importing needed packages
# https://medium.com/better-programming/how-to-extract-any-artists-data-using-spotify-s-api-python-and-spotipy-4c079401bc37

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 

# credential declaration - get your own API access codes

client_id = 'Client ID here'
client_secret = 'Secret ID here'

cred_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager = cred_manager)

def getTrackIDs(user, playlist_id):
    '''
    Returns a list of track IDs for all tracks in playlist playlist_id.
    user: the Spotify user that created the playlist.
    playlist_id: the unique identifier for the playlist we want to work with.
    '''
    ids = []
    playlist = sp.user_playlist(user, playlist_id)

    for i in playlist['tracks']['items']:
        track = i['track']
        ids.append(track['id'])

    return ids

ids = getTrackIDs('caledfwitch', '4fJYjNMMTZObKBXeIgknfO')

def getTrackFeatures(id):
    '''
    Takes a Spotify track's unique ID and returns a list with all its info.
    id: The track's unique ID.
    '''
    meta = sp.track(id)
    features = sp.audio_features(id)

    # meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']

    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']

    track = [name, album, artist, release_date, length, popularity, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
    return track

# Create nested list of all tracks in ids

tracks = []

for i in range(len(ids)):
    time.sleep(.5)
    track = getTrackFeatures(ids[i])
    tracks.append(track)

# Create CSV file

df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
df.to_csv("marias.csv", sep = ',')