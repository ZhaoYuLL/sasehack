import os
import base64
import requests
import json
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import sys
from spotipy.oauth2 import SpotifyOAuth



client_id = "421eb82f969d48b88440ff24ff4c581b"
client_secret = "35fd513f451f49a39b4895e392da85be"

redirect_uri = "http://localhost:8888/callback"


# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def generate_track_list(mE):
    # Generate a list of 10 random track URIs
    if mE == 'angry':
        scale = 'energy'
        lb, ub = 0, 0.3
    elif mE == 'happy':
        scale = 'danceability'
        lb, ub = 0.7, 1
    elif mE == 'sad':
        scale = 'valence'
        lb, ub = 0.7, 1
    elif mE == 'neutral':
        scale = 'valence'
        lb, ub = 0.7, 1
    else:
        scale = 'danceability'
        lb, ub = 0.7, 1

    random_track_uris = []

    while len(random_track_uris) < 10:
        random_offset = random.randint(0, 100)

        search_query = random.choice('abcdefghijklmnopqrstuvwxyz') + "%"

        results = sp.search(q=search_query, type="track", limit=1, offset=random_offset)
        tracks = results.get("tracks", {}).get("items", [])

        if tracks:
            audio_features = sp.audio_features(tracks[0]["uri"])[0]
            val = audio_features[scale]
            if lb <= val <= ub and tracks[0]["uri"] not in random_track_uris:
                random_track_uris.append(tracks[0]["uri"])

    return random_track_uris



# Print the list of random track URIs
def display_tracks(tracks):
    for i, track_uri in enumerate(tracks, start=1):
        track_info = sp.track(track_uri)

        artist_names = []
        for artist in track_info["artists"]:
            artist_names.append(artist["name"])

        artist_names = ", ".join(artist_names)
        track_name = track_info["name"]

        # Print the track information
        print(f"{i}. Artist(s): {artist_names}")
        print(f"   Track: {track_name}")



#display_tracks(generate_track_list('angry'))



