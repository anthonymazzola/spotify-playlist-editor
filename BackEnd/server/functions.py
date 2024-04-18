import requests
from tokens import CLIENT_ID , CLIENT_SECRET, REDIRECT_URI
import spotipy
import spotipy.util as util
from urllib.parse import urlparse
import re
import track as Track
import json

#authorization get token that gives permission to access user info
#sp must be either a global variable or passed back to app.py
def authorization():
    username = " "
    while (username.isspace()):
        username = input("Please enter your spotify Username: ")
    token = util.prompt_for_user_token(username,'playlist-modify-public user-library-read',client_id = CLIENT_ID,client_secret = CLIENT_SECRET,redirect_uri = REDIRECT_URI)
    
    if token:
        #if choosen to be global
        global sp
        sp = spotipy.Spotify(auth=token)
    #if chossen to be passed back
    return sp


def url_parser(url):
    parsed = urlparse(url)
    playlistID = re.search(r'/(playlist|artist|album|track)/([^/]+)', parsed.path).group(2)
    return playlistID

def get_playlist_id(spotify_url):
    # Use regular expressions to extract the playlist ID
    match = re.search(r'/(playlist|artist|album|track)/([^/?]+)', spotify_url)
    if match:
        playlist_id = match.group(1)
        return playlist_id
    else:
        # If no match is found, return None or raise an exception, depending on your preference
        return None

#can pass in url or prompt user for it
#returns list of track objects              
def get_playlist(url):
        url = input("Please enter the playlist URL:")
        #parses url
        playlistID = url_parser(url)
        #returns tracks
        tracks = sp.playlist_tracks(str(playlistID),fields='items.track')

        # Iterate through the list of tracks and extract artist names
        #parses through to get track name, aritsit, popularity
        tracks_in_playlist = []
        for track_info in tracks["items"]:
            artist_name = track_info['track']['album']['artists'][0]['name']
            track_name = track_info['track']['name']
            popularity = track_info['track']['popularity']
            trackID = track_info['track']['id']
            track = track(track_name, artist_name, trackID, popularity)
            print(track)
            tracks_in_playlist.append(track)
        
        return tracks_in_playlist
    
    
#need this for implimenting deletion: user_playlist_remove_all_occurrences_of_tracks()

url1 = "https://open.spotify.com/playlist/0DGFt5fue3tSqXlWwiBJd2"
url2 = "https://open.spotify.com/playlist/0DGFt5fue3tSqXlWwiBJd2?si=14ae45fef6d5462d"

playlist_id1 = get_playlist_id(url1)
playlist_id2 = get_playlist_id(url2)

print("Playlist ID 1:", playlist_id1)
print("Playlist ID 2:", playlist_id2)