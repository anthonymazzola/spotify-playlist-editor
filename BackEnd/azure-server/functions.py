import random
import string
from urllib.parse import urlparse
import re
import matplotlib.pyplot as plt
from io import BytesIO
import base64

import spotipy
import spotipy.util as util
from datetime import datetime


#handles both url from search bar and share function
def url_parser(url):
    parsed = urlparse(url)
    playlistID = re.search(r'/(playlist|artist|album|track)/([^/]+)', parsed.path).group(2)
    return playlistID

def createStateKey(size):
	#https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
	return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))



#for testing purposes:
sampleJson= {
    "tracks": [
        {
            "artist_name": "Artist 1",
            "track_name": "Track 1",
            "image": "image 1",
            "track_id": "2ZWlPOoWh0626oTaHrnl2a"
        },
        {
            "artist_name": "Artist 2",
            "track_name": "Track 2",
            "image": "image 2",
            "track_id": "6FBzhcfgGacfXF3AmtfEaX"
        },
        {
            "artist_name": "Artist 3",
            "track_name": "Track 3",
            "image": "image 3",
            "track_id": "01z2fBGB8Hl3Jd3zXe4IXR"
        },
        {
            "artist_name": "Artist 4",
            "track_name": "Track 4",
            "image": "image 4",
            "track_id": "6kf7ZCJjEbjZXikivKOsvJ"
        },
        {
            "artist_name": "Artist 5",
            "track_name": "Track 5",
            "image": "image 5",
            "track_id": "3xKsf9qdS1CyvXSMEid6g8"
        },
        {
            "artist_name": "Artist 6",
            "track_name": "Track 6",
            "image": "image 6",
            "track_id": "3GZD6HmiNUhxXYf8Gch723"
        },
        {
            "artist_name": "Artist 7",
            "track_name": "Track 7",
            "image": "image 7",
            "track_id": "1OubIZ0ARYCUq5kceYUQiO"
        }
    ]
}

trackData = [
        {
            "artist_name": "Artist 1",
            "track_name": "Track 1",
            "image": "image 1",
            "track_id": "2ZWlPOoWh0626oTaHrnl2a",
            "loudness": -9.584,
            "tempo": 116.408,
            "energy": 0.386,
            "track_popularity": 83,
            "release_date": 2020
        },
        {
            "artist_name": "Artist 2",
            "track_name": "Track 2",
            "image": "image 2",
            "track_id": "6FBzhcfgGacfXF3AmtfEaX",
            "loudness": -9.584,
            "tempo": 116.408,
            "energy": 0.386,
            "track_popularity": 83,
            "release_date": 2021
        },
        {
            "artist_name": "Artist 3",
            "track_name": "Track 3",
            "image": "image 3",
            "track_id": "01z2fBGB8Hl3Jd3zXe4IXR",
            "loudness": -9.584,
            "tempo": 116.408,
            "energy": 0.386,
            "track_popularity": 83,
            "release_date": 2014
        },
        {
            "artist_name": "Artist 4",
            "track_name": "Track 4",
            "image": "image 4",
            "track_id": "6kf7ZCJjEbjZXikivKOsvJ",
            "loudness": -9.584,
            "tempo": 116.408,
            "energy": 0.386,
            "track_popularity": 40,
            "release_date": 2000
        },
        {
            "artist_name": "Artist 5",
            "track_name": "Track 5",
            "image": "image 5",
            "track_id": "3xKsf9qdS1CyvXSMEid6g8",
            "loudness": -9.584,
            "tempo": 116.408,
            "energy": 0.386,
            "track_popularity": 83,
            "release_date": 2018
        },
        {
            "artist_name": "Artist 6",
            "track_name": "Track 6",
            "image": "image 6",
            "track_id": "3GZD6HmiNUhxXYf8Gch723",
            "loudness": -9.584,
            "tempo": 116.408,
            "energy": 0.386,
            "track_popularity": 23,
            "release_date": 2017
        },
        {
            "artist_name": "Artist 7",
            "track_name": "Track 7",
            "image": "image 7",
            "track_id": "1OubIZ0ARYCUq5kceYUQiO",
            "loudness": -9.584,
            "tempo": 116.408,
            "energy": 0.386,
            "track_popularity": 80,
            "release_date": 2016
        }
    ]

#for testing-----------
token = "BQB4EO3IPDIqGBSa7hcF1cIAKwkaUARwnmqi8qKr5whr4hLqkfRzXr_QlPrWkwN-5-Xn6bFvBQKNNboDkGuUlIpBrMPTO6UADwnnm2Ug_FRcJgYvSDE"
#-----------------------

def make_graphs(track_data):
   #get artist count for artist frequency 
    artist_count = {}
    for track in track_data:
        artist = track['artist_name']
        if(artist_count.get(artist) == None):
            artist_count[artist] = artist_count.get(artist,0) + 1
        else:
            artist_count[artist] = artist_count.get(artist) + 1

    #list of encoded urls being returned
    returnImages= []
    
    #creating graph for artist frequency
    fig1 = plt.figure()
    top_artists = dict(sorted(artist_count.items(), key=lambda item: item[1], reverse=True)[:3])
    plt.bar(top_artists.keys(), top_artists.values())
    plt.xlabel('Artist')
    plt.ylabel('Frequency')
    plt.title('Top 3 Artist Frequency in Playlist')
    plt.xticks(rotation=45)
    img1 = BytesIO()
    plt.savefig(img1, format = 'png')
    plt.close()
    img1.seek(0)
    plot_url1 = base64.b64encode(img1.getvalue()).decode('utf8')
    #print(plot_url1)
    returnImages.append(plot_url1)
    #plt.show()
    #fig1.savefig('./assets/artist_occ.png')

    loudness = [track["loudness"] for track in track_data]
    tempo = [track['tempo'] for track in track_data]
    energy = [track['energy'] for track in track_data]
  
    # Then you would want to isolate the ones in the bottom left corner 
    # As it would be the quietest and slowest songs 
    # Or can look for the upbeat music -> top right corner of graph
    fig2 = plt.figure()
    plt.scatter(loudness, tempo, c=energy, cmap='viridis', alpha=0.7)
    plt.xlabel('Loudness (dB)')
    plt.ylabel('Tempo (BPM)')
    plt.title('Audio Attributes')
    plt.colorbar(label='Energy')
    img2 = BytesIO()
    plt.savefig(img2, format = 'png')
    plt.close()
    img2.seek(0)
    plot_url2 = base64.b64encode(img2.getvalue()).decode('utf8')
    #print(plot_url2)
    returnImages.append(plot_url2)
    
    #graph for boxplot of loudness
    fig3 = plt.figure()
    plt.boxplot(x = loudness)
    plt.xlabel("Loudness")
    plt.ylabel("Decibels")
    plt.title('loudness of the playlist')
    img3 = BytesIO()
    plt.savefig(img3, format = 'png')
    plt.close()
    img3.seek(0)
    plot_url3 = base64.b64encode(img3.getvalue()).decode('utf8')
    #print(plot_url3)
    returnImages.append(plot_url3)
    
    return returnImages
    
"""     #graph for boxplot of loudness
    fig4 = plt.figure()
    plt.scatter(release_dates, popularity)
    plt.xlabel("release dates")
    plt.ylabel("popularity level (0 - 100)")
    plt.title('Popularity Levels During a Year')
    img4 = BytesIO()
    plt.savefig(img4, format = 'png')
    plt.close()
    img4.seek(0)
    plot_url4 = base64.b64encode(img4.getvalue()).decode('utf8')
    returnImages.append(plot_url4) """


    
def get_mood_tracks(mood, audio_features):
    moodtrackIDs = []
    
    if (mood == "calm"):
        #calm: 'loudness'
        for feature in audio_features:
            if (feature['loudness'] <= -20):
                moodtrackIDs.append(feature['id'])
                
    if (mood == "upbeat"):
        #upbeat/energetic: energy': 0.386
        for feature in audio_features:
            if (feature['energy'] >= .70):
                moodtrackIDs.append(feature['id'])
                
    if (mood == "dancy"):
        for feature in audio_features:
            if (feature['danceability'] >= .70):
                moodtrackIDs.append(feature['id'])
        #dancy : 'danceability': 0.575
        
    if (mood == "running"):
        #running: 'tempo':BPM 130-180
        for feature in audio_features:
            if (130 <=feature['tempo'] <= 180):
                moodtrackIDs.append(feature['id'])
                
    if (mood == "instrumental"):
        #istramental: instramentalness 1= more
        for feature in audio_features:
            if (feature['instrumentalness'] >= .700):
                moodtrackIDs.append(feature['id'])
    
    

    return moodtrackIDs
    
#audio_features = make_graphs()
#ids = get_mood_tracks("instrumental", audio_features)
#Print(ids)
#create_playlist()

#make_graphs(trackData)
