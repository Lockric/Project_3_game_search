import requests
from heapsort import HeapSort
from mergesort import MergeSort
from igdb.wrapper import IGDBWrapper
from igdb.igdbapi_pb2 import GameResult
from igdb.igdbapi_pb2 import PlatformResult

# information for accessing the data base
ClientID = 'vmqipli3y2vhqnenur94vvzdk8eqhs'
ClientSecret = 'gphrec7hscngppx4heaoiukjsnkclc'
r = requests.post(f'https://id.twitch.tv/oauth2/token?client_id={ClientID}&client_secret={ClientSecret}&grant_type=client_credentials')

# get access to igdb reques
json_reponse = r.json()
access_token = json_reponse['access_token']
wrapper = IGDBWrapper(ClientID, access_token)

'''
# Protobuf API request
byte_array = wrapper.api_request(
            'games.pb', # Note the '.pb' suffix at the endpoint
            'fields id, name; offset 0; where genres=12;'
          )
games_message = GameResult()
games_message.ParseFromString(byte_array) # Fills the protobuf message object with the response
games = games_message.games
print(games)
'''

# Initialize an empty list to store game data
all_games = []

# Initial API request (you've already done this)
byte_array = wrapper.api_request(
    'games.pb',
    'fields id, name, rating, genres; offset 0; where name="Spider-Man";'
)
games_message = GameResult()
games_message.ParseFromString(byte_array)
all_games.extend(games_message.games)  # Add the initial results to the list
#print(all_games)


# Make additional requests with increased offset
# For example, let's fetch the next 10 results
next_offset = 10
for i in range (0, 3, 1):
    byte_array = wrapper.api_request(
        'games.pb',
        f'fields id, name, rating, genres; offset {next_offset}; where name="Spider-Man";'
    )
    games_message.ParseFromString(byte_array)
    if not games_message.games:
        break  # No more results, exit the loop
    all_games.extend(games_message.games)  # Add the new results to the list
    next_offset += 10  # Increase the offset for the next request

# Now 'all_games' contains all the concatenated results
for game in all_games:
    print(f"Game ID: {game.id}, Name: {game.name}, rating: {game.rating}")

# You can process the combined data further as needed

byte_array = wrapper.api_request(
    'platforms.pb',
    'fields id, name; offset 0;'
)

platforms = []
platform_message = PlatformResult()
platform_message.ParseFromString(byte_array) # Fills the protobuf message object with the response
platforms.extend(platform_message.platforms)

next_offset = 10
while True:
    byte_array = wrapper.api_request(
        'platforms.pb',
        f'fields id, name; offset {next_offset};'
    )
    platform_message.ParseFromString(byte_array)
    if not platform_message.platforms:
        break  # No more results, exit the loop
    platforms.extend(platform_message.platforms)  # Add the new results to the list
    next_offset += 10  # Increase the offset for the next request

MergeSort(platforms, 0, len(platforms) - 1)

for platform in platforms:
    print(f"Platform ID: {platform.id}, Name: {platform.name}")