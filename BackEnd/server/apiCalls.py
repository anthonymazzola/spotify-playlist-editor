import requests
from tokens import CLIENT_ID , CLIENT_SECRET, REDIRECT_URI
import spotipy
import spotipy.util as util
from urllib.parse import urlparse
import re
import json




def authorization(scope):
    username = " "
    while (username.isspace()):
        username = input("Please enter your spotify Username: ")
    token = util.prompt_for_user_token(username,scope,client_id = CLIENT_ID,client_secret = CLIENT_SECRET,redirect_uri = REDIRECT_URI)
    if token:
        sp = spotipy.Spotify(auth=token)
        print(sp.me())
#-----------------------------------------------------------------------
        #loads current liked/saved songs in the library:
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])
            
        trackIDS= get_playlist(sp)
#-----------------------------------------------------------------------
        token = util.prompt_for_user_token(username, "playlist-modify-public", client_id = CLIENT_ID,client_secret = CLIENT_SECRET,redirect_uri = REDIRECT_URI)
        sp = spotipy.Spotify(auth=token)
        user_id= sp.me()['id']
        name_of_Playlist = input("please enter the name of the desired playlist:")
        newPlaylist = sp.user_playlist_create(user_id, name_of_Playlist,True)
        #playlists = sp.user_playlists(username)
        #for playlist in playlists['items']:
        #    if (playlist['name'] == str(name_of_Playlist)):
         #       playlistID = playlist["id"]
         #   else:
         #       playlistID =""
        sp.user_playlist_add_tracks(user_id, newPlaylist['id'], trackIDS)    
        
#------------------------------------------------------
#if token is not available or if user name is not exsistant  
    else:
        print("cant get token for ", username)
  
#parses input URL to get ID to retrieve data      
def url_parser(url):
    parsed = urlparse(url)
    playlistID = re.search(r'/(playlist|artist|album|track)/([^/]+)', parsed.path).group(2)
    return playlistID

   
def get_playlist(sp):
        url = input("Please enter the playlist URL:")
        playlistID = url_parser(url)
        tracks = sp.playlist_tracks(str(playlistID),fields='items.track')

# Iterate through the list of tracks and extract artist names
        artist_names = []
        track_names= []
        trackIDs = []
        for track_info in tracks["items"]:
            artist_name = track_info['track']['album']['artists'][0]['name']
            track_name = track_info['track']['name']
            track_names.append(track_name)
            artist_names.append(artist_name)
            trackIDs.append(track_info['track']['id'])
            print("track: "+str(track_name)+ " , by: "+str(artist_name))
        return trackIDs

def new_authorization():
    auth_url = 'https://accounts.spotify.com/api/token'
    data = {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
}
    auth_response = requests.post(auth_url, data=data)
    access_token = auth_response.json().get('access_token')
    headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
    base_url = 'https://api.spotify.com/v1/'
    endpoint = "playlists/0DGFt5fue3tSqXlWwiBJd2"
    
    url = ''.join([base_url,endpoint])
    
    response = requests.get(url,headers=headers)
    data = response.json()
    
    tracks = data["tracks"]["items"]
    for track in tracks:
        track_name = track["track"]["name"]
        print("Track Name:", track_name)
   

    
new_authorization()
#authorization('user-library-read')

#https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=5819a78553774c8c
# playlist_id = 37i9dQZF1DXcBWIGoYBM5M

#https://open.spotify.com/playlist/0DGFt5fue3tSqXlWwiBJd2?si=39c69d418dba4644
#https://open.spotify.com/playlist/0DGFt5fue3tSqXlWwiBJd2