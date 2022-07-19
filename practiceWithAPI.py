import requests

SPOTIFY_CREATE_PLAYLIST_URL = "https://api.spotify.com/v1/users/giselle_arboleda/playlists"
ACCESS_TOKEN = "BQCUG9Wv2GEUmcParbZopev6TigW8EzEQkqrhi0wIJFPCrObh11kSD9_KYR5s81tKucsDmxq2Ya8zK0VD8kGu3CGkRFTz02P1mmSEgwzg8rdCf9cnYIxPrd8HVotNMyiUbxmc1aGTOKDY1gG8W0Sqt9RnmFz9_F8tNFhYH-P6SyTwUvODwqbcmUqfkXUB9q1c1c0-z3gn0p4widRaSGs1QblzOQCj4_Mh0cJfQQQz1dRWD_45nOn"


def create_playlist_on_spotify(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL, headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()
    return json_resp


def main():
    playlist = create_playlist_on_spotify(
        name="My Private Playlist 365",
        public=False
    )

    print(f"Playlist: {playlist}")



if __name__ == "__main__":
    main()





