import requests
from heapsort import HeapSort
from mergesort import MergeSort
from igdb.wrapper import IGDBWrapper
from igdb.igdbapi_pb2 import GameResult
from igdb.igdbapi_pb2 import PlatformResult
from igdb.igdbapi_pb2 import GenreResult

def get_wrapper():
    # information for accessing the data base
    ClientID = 'vmqipli3y2vhqnenur94vvzdk8eqhs'
    ClientSecret = 'gphrec7hscngppx4heaoiukjsnkclc'
    r = requests.post(f'https://id.twitch.tv/oauth2/token?client_id={ClientID}&client_secret={ClientSecret}&grant_type=client_credentials')

    # get access to igdb reques
    json_reponse = r.json()
    access_token = json_reponse['access_token']
    return IGDBWrapper(ClientID, access_token)

def get_game_by_name(wrapper, name, iter):
    gameList = []
    games_message = GameResult()
    next_offset = 0
    if iter >= 0:
        for i in range (0, iter):
            byte_array = wrapper.api_request(
                'games.pb',
                f'fields id, name, rating; offset {next_offset}; where name="{name}";'
            )
            games_message.ParseFromString(byte_array)
            if not games_message.games:
                break  # No more results, exit the loop
            gameList.extend(games_message.games)  # Add the new results to the list
            next_offset += 10  # Increase the offset for the next request
    else:
        while True:
            byte_array = wrapper.api_request(
                'games.pb',
                f'fields id, name, rating; offset {next_offset}; where name="{name}";'
            )
            games_message.ParseFromString(byte_array)
            if not games_message.games:
                break  # No more results, exit the loop
            gameList.extend(games_message.games)  # Add the new results to the list
            next_offset += 10  # Increase the offset for the next request
    return gameList

def get_game_by_genre(wrapper, genreId, iter):
    gameList = []
    games_message = GameResult()
    next_offset = 0
    if iter >= 0:
        for i in range (0, iter):
            byte_array = wrapper.api_request(
                'games.pb',
                f'fields id, name, rating, genres; offset {i}; where genres={genreId};'
            )
            games_message.ParseFromString(byte_array)
            if not games_message.games:
                break  # No more results, exit the loop
            gameList.extend(games_message.games)  # Add the new results to the list
            next_offset += 10  # Increase the offset for the next request
    else:
        while True:
            byte_array = wrapper.api_request(
                'games.pb',
                f'fields id, name, rating; offset {next_offset}; where genres={genreId};'
            )
            games_message.ParseFromString(byte_array)
            if not games_message.games:
                break  # No more results, exit the loop
            gameList.extend(games_message.games)  # Add the new results to the list
            next_offset += 10  # Increase the offset for the next request
    return gameList

def get_game_by_platform(wrapper, platId, iter):
    gameList = []
    games_message = GameResult()
    next_offset = 0
    if iter >= 0:
        for i in range (0, iter):
            byte_array = wrapper.api_request(
                'games.pb',
                f'fields id, name, rating; offset {next_offset}; where platforms={platId};'
            )
            games_message.ParseFromString(byte_array)
            if not games_message.games:
                break  # No more results, exit the loop
            gameList.extend(games_message.games)  # Add the new results to the list
            next_offset += 10  # Increase the offset for the next request
    else:
        while True:
            byte_array = wrapper.api_request(
                'games.pb',
                f'fields id, name, rating, genres; offset {next_offset}; where platforms={platId};'
            )
            games_message.ParseFromString(byte_array)
            if not games_message.games:
                break  # No more results, exit the loop
            gameList.extend(games_message.games)  # Add the new results to the list
            next_offset += 10  # Increase the offset for the next request
    return gameList

def get_genre_list(wrapper):
    genreList = []
    genreMessage = GenreResult()
    next_offset = 0
    while True:
        byte_array = wrapper.api_request(
            'genres.pb',
            f'fields id, name; offset {next_offset};'
        )
        genreMessage.ParseFromString(byte_array)
        if not genreMessage.genres:
            break
        genreList.extend(genreMessage.genres)
        next_offset += 10
    return genreList

def get_platform_list(wrapper):
    platformList = []
    platformMessage = PlatformResult()
    next_offset = 0
    while True:
        byte_array = wrapper.api_request(
            'platforms.pb',
            f'fields id, name; offset {next_offset};'
        )
        platformMessage.ParseFromString(byte_array)
        if not platformMessage.platforms:
            break  # No more results, exit the loop
        platformList.extend(platformMessage.platforms)  # Add the new results to the list
        next_offset += 10  # Increase the offset for the next request
    return platformList

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

HeapSort(platforms)

for platform in platforms:
    print(f"Platform ID: {platform.id}, Name: {platform.name}")
'''
