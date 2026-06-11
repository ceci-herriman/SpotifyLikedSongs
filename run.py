import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

scope = "user-library-read playlist-modify-public playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

TOP_X = 50 #how many of the most recent liked songs to retrieve 

##get TOP_X most recent liked songs 
likedSongs = sp.current_user_saved_tracks(limit=TOP_X)
tracks = []

for song in likedSongs['items']: 
    tracks.append(song['track']['id'])

##open Live Liked Songs playlist and add 
livePlaylistId = '1t5rNLbkrzHlyH1z6fldmr'
sp.playlist_replace_items(livePlaylistId, tracks)

print("done updating!")