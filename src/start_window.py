import pygame
import pygame.freetype
from display_functions import *

from api_call_back import *
from heapsort import HeapSort
from mergesort import MergeSort

# For this file the reference is Project 4: Sudoku, COP3502. Based the window and buttons on that project

# This function takes in the result for genre considering all the buttons for genre
def show_results_genre(genre):
    # Set up the display with the fonts necessary
    result_screen = pygame.display.set_mode((600, 700))
    font_message = pygame.freetype.SysFont(None, 25)
    font_results = pygame.freetype.SysFont(None, 15)
    clock = pygame.time.Clock()
    done = False
    # Creating buttons for merge and heap sort needed in the second window
    heapsort_button = pygame.Rect(137, 100-15, 150, 50)
    mergesort_button = pygame.Rect(313, 100-15, 150, 50)
    box = pygame.Rect(00, 00, 600, 145)

    # Initialize the coordinate and speed for scrolling, when the window has more infomtion than it can cover
    content_y = 0
    scroll_speed = 100

    # Get the wrapper from the api key to recive the needed information, tuple here was needed to not add extra functions
    wrapper = get_wrapper()
    # Offset set to 100 as there are a lot of games that do have a rating as of yet
    results = get_game_by_genre(wrapper, genre[1], 100)

    # Need the while loop to loop into the main event with the mouse clicking and mouse scroll
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if heapsort_button.collidepoint(event.pos):
                    print("Heap Sort button clicked")
                    HeapSort(results)
                elif mergesort_button.collidepoint(event.pos):
                    print("Merge Sort button clicked")
                    MergeSort(results, 0, len(results) - 1)
            elif event.type == pygame.MOUSEWHEEL:
                if event.y > 0:  # scroll up
                    content_y = min(content_y + scroll_speed, 0)
                elif event.y < 0:  # scroll down
                    content_y = max(content_y - scroll_speed, -(len(results) * 20 - 145))

        # Create the window with all the needed buttons 
        result_screen.fill((81, 90, 115))
        # Added the scrolling function here so that not all the window can be scrollable 
        build_string_results(result_screen, results, font_results, (255, 255, 255), (box.x + 5, box.y + content_y + 5))
        draw_box(result_screen, (154, 170, 217), box)
        draw_text(result_screen, f"Results for {genre[0]}:", font_message, (0, 0, 0), (182, 50-15))
        draw_button(result_screen, "Heap Sort", font_message, (67, 45, 115), heapsort_button)
        draw_button(result_screen, "Merge Sort", font_message, (67, 45, 115), mergesort_button)
        pygame.display.flip()
        clock.tick(30)

# This function takes in the result for platform same as the genre above
def show_results_platform(platform):
    # There is no difference but the api value that is platform in this case here 
    result_screen = pygame.display.set_mode((600, 700))
    font_message = pygame.freetype.SysFont(None, 25)
    font_results = pygame.freetype.SysFont(None, 15)
    clock = pygame.time.Clock()
    done = False

    heapsort_button = pygame.Rect(137, 100-15, 150, 50)
    mergesort_button = pygame.Rect(313, 100-15, 150, 50)
    box = pygame.Rect(00, 00, 600, 145)
    content_y = 0
    scroll_speed = 100

    wrapper = get_wrapper()
    # Offset set to 100 as there are a lot of games that do have a rating as of yet
    results = get_game_by_platform(wrapper, platform[1], 100)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if heapsort_button.collidepoint(event.pos):
                    print("Heap Sort button clicked")
                    HeapSort(results)
                elif mergesort_button.collidepoint(event.pos):
                    print("Merge Sort button clicked")
                    MergeSort(results, 0, len(results) - 1)
            elif event.type == pygame.MOUSEWHEEL:
                if event.y > 0:  # scroll up
                    content_y = min(content_y + scroll_speed, 0)
                elif event.y < 0:  # scroll down
                    content_y = max(content_y - scroll_speed, -(len(results) * 20 - 145))

        result_screen.fill((81, 90, 115))
        build_string_results(result_screen, results, font_results, (255, 255, 255), (box.x + 5, box.y + content_y + 5))
        draw_box(result_screen, (154, 170, 217), box)
        draw_text(result_screen, f"Results for {platform[0]}:", font_message, (0, 0, 0), (182, 50-15))
        draw_button(result_screen, "Heap Sort", font_message, (67, 45, 115), heapsort_button)
        draw_button(result_screen, "Merge Sort", font_message, (67, 45, 115), mergesort_button)
        pygame.display.flip()
        clock.tick(30)        

# This function takes the result based on name. Keep in mind this is case sensitive
def show_results_name(name):
    # No changes from the other two function but here we have no scroll as there is no need 
    result_screen = pygame.display.set_mode((600, 700))
    font_message = pygame.freetype.SysFont(None, 25)
    font_results = pygame.freetype.SysFont(None, 15)
    clock = pygame.time.Clock()
    done = False

    heapsort_button = pygame.Rect(137, 100-15, 150, 50)
    mergesort_button = pygame.Rect(313, 100-15, 150, 50)
    box = pygame.Rect(00, 00, 600, 145)

    # Get the results from the API
    wrapper = get_wrapper()
    results = get_game_by_name(wrapper, name, 5)

    # build array of result boxes

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if heapsort_button.collidepoint(event.pos):
                    print("Heap Sort button clicked")
                    HeapSort(results)
                elif mergesort_button.collidepoint(event.pos):
                    print("Merge Sort button clicked")
                    MergeSort(results, 0, len(results) - 1)

        result_screen.fill((81, 90, 115))
        build_string_results(result_screen, results, font_results, (255, 255, 255), (25, 150))
        draw_box(result_screen, (154, 170, 217), box)
        draw_text(result_screen, f"Results for {name}:", font_message, (0, 0, 0), (182, 50-15))
        draw_button(result_screen, "Heap Sort", font_message, (67, 45, 115), heapsort_button)
        draw_button(result_screen, "Merge Sort", font_message, (67, 45, 115), mergesort_button)
        pygame.display.flip()
        clock.tick(30)

# This function implement both the start and all the buttons
def start(screen):
    font_title = pygame.freetype.SysFont(None, 35)
    font_message = pygame.freetype.SysFont(None, 25)
    clock = pygame.time.Clock()
    # Boxes and buttons needed
    input_box = pygame.Rect(200, 150, 375, 50)
    button_game = pygame.Rect(25, 150, 150, 50)
    button_genre = pygame.Rect(137, 225, 150, 50)
    button_platform = pygame.Rect(313, 225, 150, 50)
    # Define the inactive and active colors
    color_inactive = pygame.Color('black')
    color_active = pygame.Color('black')
    color = color_inactive
    # Initialize active flag and text to empty
    active = False
    text = ''
    done = False

    # There are two for loop that take the names for each genre and platfrom we are printing values for
    genre_buttons = [pygame.Rect(137, 285 + i*60, 150, 50) for i in range(6)]
    # Each genre has the value of id and is a tuple to not add extra functions
    genres = [["Fighting", 4], ["RPG", 12], ["Sports", 14], ["Shooter", 5], ["Racing", 10], ["Strategy", 15]]
    
    platform_buttons = [pygame.Rect(313, 285 + i*60, 150, 50) for i in range(6)]
    # Each platform has the value of id and is a tuple to not add extra functions
    platform = [["PS5", 167], ["PS4", 48], ["Xbox One", 49], ["Xbox Series",169], ["Switch", 130], ["PC", 6]]

    # While loop that has all the events for the buttons
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                # Added prints here to make sure the buttons were clicked 
                elif button_game.collidepoint(event.pos):
                    print("Name button clicked")
                    
                elif button_genre.collidepoint(event.pos):
                    print("Genre button clicked")

                elif button_platform.collidepoint(event.pos):
                    print("Platform button clicked")
                    
                else:
                    # Deactivate the box if anything else is clicked
                    active = False
                color = color_active if active else color_inactive

                # There are two for loop to check if a button was clicked and it then takes in the results that should be shown at the second window
                for i in range(len(genre_buttons)):
                    if genre_buttons[i].collidepoint(event.pos):
                        print(f"{genres[i]} button clicked")
                        show_results_genre(genres[i])

                for i in range(len(platform_buttons)):
                    if platform_buttons[i].collidepoint(event.pos):
                        print(f"{platform[i]} button clicked")
                        show_results_platform(platform[i])

            # This loop takes the input of the box and present the second window with the results needed
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        show_results_name(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        # Fills the screen with the title and all the buttons
        screen.fill((154, 170, 217))
        dark_blue = pygame.Color(67, 45, 115)
        draw_text(screen, "Welcome to GS Ultimate!", font_title, (0, 0, 0), (25, 25))
        draw_text(screen, "Please choose one of the following:", font_message, (0, 0, 0), (70, 80))
        pygame.draw.rect(screen, color, input_box, 2)
        draw_text(screen, text, font_message, (0, 0, 0), input_box.topleft)
        draw_button(screen, "Name:", font_message, dark_blue, button_game)  
        draw_button(screen, "Genre:", font_message, dark_blue, button_genre)  
        draw_button(screen, "Platform:", font_message, dark_blue, button_platform)   
       
        for i in range(6):
            draw_button(screen, genres[i][0], font_message, dark_blue, genre_buttons[i])
        
        for i in range(6):
            draw_button(screen, platform[i][0], font_message, dark_blue, platform_buttons[i])
        pygame.display.flip()
        clock.tick(30)
