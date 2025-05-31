import requests
import configparser
import math

# auth
import base64

# globals
token = None
class App:
    def __init__(self):
        self.get_token()
        if self.token == None:
            print("Couldn't get token!")
            exit()

    def get_token(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        client_id = config.get("spotify_secrets", "client_id")
        client_secret = config.get("spotify_secrets", "client_secret")
# Encode credentials
        auth_str = f"{client_id}:{client_secret}"
        b64_auth_str = base64.b64encode(auth_str.encode()).decode()

# Set up headers and data
        headers = {
            'Authorization': f'Basic {b64_auth_str}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            'grant_type': 'client_credentials'
        }

# Send the POST request
        response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

        token = None
# Handle response
        if response.status_code == 200:
            token = response.json()['access_token']
        self.token = token

#
    def fetch_web_api(self, endpoint: str):
        url = f'https://api.spotify.com/{endpoint}'
        headers = {
            'Authorization': f'Bearer {self.token}',
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_playlist_tracks(self, playlist_id) -> list[dict]:
        """
        Returns all the tracks in the playlist, to be more precise: track artists and track name

        Args:
            playlist_id(str) - id of the playlist
        Returns:
            list[{artists(list(str)), name(str)}]
        """
        num_of_tracks = self.get_number_of_tracks_in_playlist(playlist_id)
        times_to_offset = math.ceil(num_of_tracks/50.)
        res = []
        for offset in range(0, times_to_offset):
            data = self.fetch_web_api(f'v1/playlists/{playlist_id}/tracks?offset={offset*50}&limit=50')
            for i in data.get("items"):
                obj = {}
                obj['artists'] = [artist['name'] for artist in i['track']['artists']]
                obj['name'] = i['track']['name']
                res.append(obj)
        return res
    def get_number_of_tracks_in_playlist(self, playlist_id) -> int:
        """
        Returns the number of tracks in the playlist 

        Args:
            playlist_id(str) - id of the playlist
        Returns:
            number of tracks
        """
        data = self.fetch_web_api(f'v1/playlists/{playlist_id}')
        return data.get("tracks")['total']

def print_tracks(tracks: list[dict]):
    for track in tracks:
        for artist in track['artists']:
            print(artist, end=' ')
        print(f" | {track['name']}")

def track_to_arr_str(tracks):
    res = []
    for track in tracks:
        str_r = ""
        for artist in track['artists']:
            str_r += artist
            str_r += " "
        str_r += f" {track['name']}"
        res.append(str_r)
    return res

if __name__ == "__main__":
    app = App()
    # tracks = app.get_playlist_tracks('23cMVZslIc26puFc10KjcH')
    tracks = app.get_playlist_tracks('3gHIyBVPhS1p1er6tYpXmQ')
    # print(app.get_number_of_tracks_in_playlist('3gHIyBVPhS1p1er6tYpXmQ'))
    print_tracks(tracks)

