
class Track:
    def __init__(self, name, artist, id, popularity):
        self.name = name
        self.artist = artist
        self.id = id
        self.popularity = popularity
        
        
    def __str__(self):   
        return "track: "+str(track_name)+ " , by: "+str(artist_name)+ " , with popularity: "+str(popularity)