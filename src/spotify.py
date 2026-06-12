# ライブラリのインポート
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# import time
import requests
from requests.exceptions import HTTPError
import pandas as pd

# クライアントIDとクライアントシークレットを設定
client_id = 'c1f950b505e64e6fb20c038bd86721bd'
client_secret = '0853dbd65fba4d01ad9afd4441ef9b75'



import requests
from spotipy.oauth2 import SpotifyClientCredentials

auth = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

token = auth.get_access_token()

r = requests.get(
    "https://api.spotify.com/v1/playlists/37i9dQZF1DXcBWIGoYBM5M",
    headers={
        "Authorization": f"Bearer {token}"
    }
)

print(r.status_code)
print(r.text[:1000])