import pygame
import pygame.freetype
from display_functions import draw_button
from display_functions import draw_text

def display(screen):
    font_title = pygame.freetype.SysFont(None, 35)
    font_message = pygame.freetype.SysFont(None, 25)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(200, 150, 375, 50)
    button_game = pygame.Rect(25, 150, 150, 50)
    button_genre = pygame.Rect(137, 225, 150, 50)
    button_platform = pygame.Rect(313, 225, 150, 50)
    color_inactive = pygame.Color('black')
    color_active = pygame.Color('black')
    color = color_inactive
    active = False
    text = ''
    done = False

    genre_buttons = [pygame.Rect(137, 285 + i*60, 150, 50) for i in range(6)]
    genres = ["Action", "RPG", "Sports", "Shooter", "Racing", "Strategy"]
    

    platform_buttons = [pygame.Rect(313, 285 + i*60, 150, 50) for i in range(6)]
    platform = ["PS5", "PS4", "Xbox One", "Xbox Series", "Switch", "PC"]

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                elif button_game.collidepoint(event.pos):
                    print("Name button clicked")
                    
                elif button_genre.collidepoint(event.pos):
                    print("Genre button clicked")
                    
                elif button_platform.collidepoint(event.pos):
                    print("Platform button clicked")
                    
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((154, 170, 217))
        dark_blue = pygame.Color(67, 45, 115)
        draw_text(screen, "Welcome to IGDB Project!", font_title, (0, 0, 0), (25, 25))
        draw_text(screen, "Please choose one of the following:", font_message, (0, 0, 0), (70, 80))
        pygame.draw.rect(screen, color, input_box, 2)
        draw_text(screen, text, font_message, (0, 0, 0), input_box.topleft)
        draw_button(screen, "Name", font_message, dark_blue, button_game)  
        draw_button(screen, "Genre", font_message, dark_blue, button_genre)  
        draw_button(screen, "Platform", font_message, dark_blue, button_platform)   
       
        for i in range(6):
            draw_button(screen, genres[i], font_message, dark_blue, genre_buttons[i])
        
        for i in range(6):
            draw_button(screen, platform[i], font_message, dark_blue, platform_buttons[i])
        pygame.display.flip()
        clock.tick(30)