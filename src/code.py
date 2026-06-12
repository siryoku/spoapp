# import requests

# def sum_numbers(a, b):
#   return (a + b), a

# def get_json_data(id):
#   res = requests.get('http://xxxx', param={'id':id})
#   res_json = res.json()
#   return res_json

# def get_user_names(user_ids):
#   user_names = {}
#   for id in user_ids:
#     json_data = get_json_data(id)
#     user_names[id] = json_data['name']
#   return user_names

# def user_name_validation(user_name):
#   if user_name == None:
#     raise ValueError('名前が設定されていません')


# def add(a, b):
  # return a + b

# def is_adult(age):
#   return age >= 18

# def divide(a, b):
#   return a / b

def multiply(a, b):
  return a * b

def is_even(num):
    return num % 2 == 0

def divide(a, b):
    return a / b

def get_json_data(user_id):
  raise NotImplementedError

def get_user_name(user_id):
  data = get_json_data(user_id)
  return data["name"]

import requests

def get_status():
  response = requests.get("https://example.com")
  return response.status_code





  # 認証情報を設定
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# sp = spotipy.Spotify(
#     auth_manager=SpotifyClientCredentials(
#         client_id=client_id,
#         client_secret=client_secret
#     )
# )

# playlist_url = 'https://open.spotify.com/playlist/37i9dQZEVXbKXQ4mDTEBXq'
# playlist_id = playlist_url.split('/')[-1].split('?')[0]  #プレイリストIDを取得
# print("-------------------------------")
# # # プレイリストの楽曲一覧を取得
# # results = sp.playlist(playlist_id)
# # playlist = sp.playlist("37i9dQZF1DXcBWIGoYBM5M")
# # print(playlist["name"])

# print(sp.artist("4q3ewBCX7sLwd24euuV69X")["name"])

# print(sp.track("4cOdK2wGLETKBW3PvgPWqT")["name"])

# print(r.status_code)
# print(r.text[:1000])

# # print("artist test")
# # print(sp.artist("4q3ewBCX7sLwd24euuV69X")["name"])

# # print("track test")
# # print(sp.track("4cOdK2wGLETKBW3PvgPWqT")["name"])

# # print("search test")
# # print(sp.search(q="Bad Bunny", type="artist", limit=1))

# # artist = sp.artist("4q3ewBCX7sLwd24euuV69X")
# search = sp.search(q="Bad Bunny", type="artist", limit=1)
# print(search)