from api_call_back import *

if __name__=="__main__":
    wrapper = get_wrapper()
    print(get_genre_list(wrapper))
    print(get_platform_list(wrapper))
    print(get_game_by_name(wrapper, "Spider-Man", 5))
    print(get_game_by_platform(wrapper, 48, 5))
    print(get_game_by_genre(wrapper, 5, 5))


