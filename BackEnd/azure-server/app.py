from flask import Flask, render_template, request, jsonify, make_response, redirect, session
from flask_cors import CORS
from tokens import CLIENT_ID , CLIENT_SECRET, REDIRECT_URI
from functions import url_parser
from functions import createStateKey, get_mood_tracks, make_graphs
import spotipy
import spotipy.util as util
from urllib.parse import urlparse
from datetime import datetime
import re
import json


app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authorize')
def authorize():
    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET
    redirect_uri = REDIRECT_URI
    scope = 'playlist-modify-public user-library-read'

    # redirect user to Spotify authorization page
    authorize_url = 'https://accounts.spotify.com/en/authorize?'
    parameters = 'response_type=code&client_id=' + client_id + '&redirect_uri=' + redirect_uri + '&scope=' + scope
    print(authorize_url+parameters)
    response = make_response(redirect(authorize_url + parameters))

    return response


# @app.route('/authorize')
# def authorization():
#     username = "xhlihtjo1hafmzo7hjcmf64bj"
#     token = util.prompt_for_user_token(username,'playlist-modify-public user-library-read',client_id = CLIENT_ID,client_secret = CLIENT_SECRET,redirect_uri = REDIRECT_URI)
#     token = localStorage.getItem("token")
#     if token:
#         #if choosen to be global
#         global sp
#         sp = spotipy.Spotify(auth=token)
#     #if chossen to be passed back
#     return sp

@app.route('/test_point', methods=['GET'])
def get_sample_json():
    try:
        with open('sample.json', 'r') as file:
            data = file.read()
            return jsonify({'data': data})
    except FileNotFoundError:
        return jsonify({'error': 'File not found'})

@app.route('/get_playlist', methods=['GET'])
def getPlaylist():
    token = request.args.get('token')
    url = request.args.get('url')
    sp = spotipy.Spotify(auth=token)
    playlistID = url_parser(url)
    tracks = sp.playlist_tracks(str(playlistID),fields='items.track')

# Iterate through the list of tracks and extract artist names
    track_info_list = []
    for track_info in tracks["items"]:
        artist_name = track_info['track']['album']['artists'][0]['name']
        track_name = track_info['track']['name']
        track_id = track_info['track']['id']
        track_image = track_info['track']['album']['images'][1]['url']
        track_popularity = track_info['track']['popularity']

        track_info_dict = {
            "artist_name": artist_name,
            "track_name": track_name,
            "track_id": track_id,
            "track_image": track_image,
            "track_popularity": track_popularity
        }

        track_info_list.append(track_info_dict)

    # Create a JSON response
    response_json = jsonify({"tracks": track_info_list})
    return response_json


@app.route('/get_graphs', methods=['GET','POST'])
def getGraphs():
    token = request.args.get('token')
    trackIDJson = request.get_json()
    trackIDs = trackIDJson.get("track_ids")
    sp = spotipy.Spotify(auth=token)
    #------------------------------------------------------
    audio_features = sp.audio_features(tracks=trackIDs)
    
    track_info_list = []
    for i in range(len(trackIDs)):
        track_info = sp.track(trackIDs[i])
       #print(track_info)
        artist_name = track_info['artists'][0]['name']
        track_name = track_info['name']
        track_id = trackIDs[i]

        track_info_dict = {
            "artist_name": artist_name,
            "track_name": track_name,
            "track_id": track_id,
            "loudness": audio_features[i]["loudness"],
            "tempo": audio_features[i]["tempo"],
            "energy": audio_features[i]["energy"],  
        }

        track_info_list.append(track_info_dict)
    
    graph_urls = make_graphs(track_info_list)
    
    return graph_urls


@app.route('/create_playlist', methods=['GET','POST'])
def create_playlist():
    trackIDJson = request.get_json()
    trackIDs = trackIDJson.get("track_ids")
    token = request.args.get('token')
    name_of_Playlist = request.args.get('nameOfPlaylist')
    mood = request.args.get('mood')
    
    sp = spotipy.Spotify(auth=token)
    user_id= sp.me()['id']
    newPlaylist = sp.user_playlist_create(user_id, name_of_Playlist,True)
    
    audio_features = sp.audio_features(tracks=trackIDs)

    #call function get_mood_tracks() to return special mood tracks based on the mood passed in
    moodTracks = get_mood_tracks(mood, audio_features)
    if (len(moodTracks)> 0):
        sp.user_playlist_add_tracks(user_id, newPlaylist['id'], moodTracks)
        url = newPlaylist['external_urls']['spotify']
    else:
        sp.user_playlist_unfollow(user_id, newPlaylist['id'])
        url = "There were no songs in the playlist that matched the desired mood"  
    
    
    return url
    
@app.route('/create_recommnedations', methods=['GET','POST'])
def create_recommendations():
    trackIDJson = request.get_json()
    trackIDs = trackIDJson.get("track_ids")
    token = request.args.get('token')
    sp = spotipy.Spotify(auth=token)
    
    recommendedSongs = sp.recommendations(seed_tracks=trackIDs, limit = 10)
    track_info_list = []
    for track_info in recommendedSongs["tracks"]:
        artist_name = track_info['artists'][0]['name']
        track_name = track_info['name']
        track_id = track_info['id']
        track_image = track_info['album']['images'][1]['url']
        track_popularity = track_info['popularity']
        release_date = track_info['album']['release_date']

        track_info_dict = {
            "artist_name": artist_name,
            "track_name": track_name,
            "track_id": track_id,
            "track_image": track_image,
            "track_popularity": track_popularity,
            "release_date" : release_date
        }

        track_info_list.append(track_info_dict)
    response_json = jsonify({"tracks": track_info_list})
    return response_json

        
if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
    