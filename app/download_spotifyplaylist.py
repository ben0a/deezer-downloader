import json
from deezer.deezer import deezerSearch, my_download_song
from ipdb import set_trace

# download Spotify playlist from Deezer

# 1. open playlist in browser https://open.spotify.com/playlist/27FeS7drPhTJAjXB13ALZa
# 2. the console shows a request to https://api.spotify.com/v1/playlists/27FeS7drPhTJAjXB13ALZa?type=track%2Cepisode&market=DE (with an Authentication Token)
# 3. save the response as json
#
#j = json.load(open("spotify/test.json"))
j = json.load(open("spotify/test3.json"))
#for song_data in j['tracks']['items']:
for song_data in j['items']:
    track = song_data['track']
    title = track['name']
    artist = track['artists'][0]['name']
    together = "{} - {}".format(artist, title)
    print(together)
    try:
        song = deezerSearch(together, "track")[0]
        my_download_song(song['id'])
    except IndexError:
        print("NOTFOUND: {}".format(together))
    except Exception as e:
        print("EXCEPTION {}".format(e))


